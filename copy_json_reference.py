import re

import sublime
import sublime_plugin


SETTINGS_NAME = "CopyJSONReference.sublime-settings"


def plugin_loaded():
    # Called when the plugin is loaded
    pass


class CopyJsonReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = sublime.load_settings(SETTINGS_NAME)
        leading_dot = settings.get("leading_dot", False)
        separator = settings.get("multi_separator", "\n")

        paths = []
        for region in view.sel():
            path = self._get_path_at(view, region.end())
            if path:
                if leading_dot and not path.startswith("."):
                    path = "." + path
                elif not leading_dot and path.startswith("."):
                    path = path[1:]
                paths.append(path)

        if not paths:
            sublime.status_message("Could not determine JSON path")
            return

        result = separator.join(paths)
        sublime.set_clipboard(result)
        if len(paths) == 1:
            sublime.status_message("Copied JSON Reference: " + result)
        else:
            sublime.status_message("Copied {} JSON References".format(len(paths)))

    def _get_path_at(self, view, pos):
        scope = None
        for s in view.find_by_selector("source.json"):
            if s.contains(pos) or s.begin() <= pos <= s.end():
                scope = s
                break
        if not scope:
            return None

        text = view.substr(scope)
        offset = pos - scope.begin()
        return json_path_to(text, offset)

    def is_visible(self):
        return any(
            self.view.match_selector(region.a, "source.json")
            for region in self.view.sel()
        )

    def is_enabled(self):
        return self.is_visible()


def json_path_to(text, offset):
    """Scan JSON text up to offset and return the path string (may start with .)."""
    pos = 0
    stack = []
    is_in_key = False

    while pos < offset and pos < len(text):
        start_pos = pos
        ch = text[pos]

        if ch == '"':
            s, new_pos = _read_string(text, pos)
            if stack:
                frame = stack[-1]
                if frame["col_type"] == "object":
                    if is_in_key:
                        frame["key"] = s
                        is_in_key = False
                    elif new_pos <= offset:
                        frame.pop("key", None)
            pos = new_pos
        elif ch == "{":
            stack.append({"col_type": "object"})
            is_in_key = True
        elif ch == "[":
            stack.append({"col_type": "array", "index": 0})
        elif ch in ("}", "]"):
            if stack:
                stack.pop()
            if stack:
                frame = stack[-1]
                if frame["col_type"] == "object":
                    frame.pop("key", None)
        elif ch == ",":
            if stack:
                frame = stack[-1]
                if frame["col_type"] == "object":
                    is_in_key = True
                    frame.pop("key", None)
                elif frame["col_type"] == "array":
                    frame["index"] = frame.get("index", 0) + 1

        if pos == start_pos:
            pos += 1

    return _path_to_string(stack)


def _path_to_string(path):
    s = ""
    for frame in path:
        if frame["col_type"] == "object":
            if "key" in frame:
                key = frame["key"]
                if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", key):
                    if s:
                        s += "."
                    s += key
                else:
                    escaped = key.replace("\\", "\\\\").replace('"', '\\"')
                    s += '["' + escaped + '"]'
        else:
            idx = frame.get("index", 0)
            s += "[" + str(idx) + "]"
    return s


def _read_string(text, pos):
    p = pos + 1
    i = _find_end_quote(text, p)
    return text[p:i], i + 1


def _find_end_quote(text, i):
    while i < len(text):
        if text[i] == '"':
            bt = i
            while bt >= 0 and text[bt] == "\\":
                bt -= 1
            if (i - bt) % 2 == 0:
                break
        i += 1
    return i
