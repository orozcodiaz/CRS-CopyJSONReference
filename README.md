# CopyJSONReference

**Copy the JSON path of the node under your cursor with a single right-click.**

Right-click any key or value inside a JSON file and choose **Copy JSON Reference**.
The dotted path (e.g. `body.data.values.contact`) is instantly copied to the clipboard.

Created by **Cold Rock Software**.

---

## Features

- Context menu item that appears next to the regular **Copy** action
- Command Palette entry: `Copy JSON Reference`
- Optional keyboard shortcut (see below); none is enabled by default
- Supports nested objects **and** arrays (`body.data.items[2].name`)
- Handles keys that are not valid identifiers (`["user-id"]`, `["with space"]`)
- Multiple selections supported (paths joined by newline by default)
- Configurable leading dot and separator via settings
- Works with both pretty-printed and minified JSON
- Lightweight pure-Python scanner — no external dependencies

## Installation

### Manual

1. Download the latest release ZIP.
2. In Sublime Text go to **Preferences → Browse Packages…**
3. Extract the `CopyJSONReference` folder into the Packages directory.
4. Restart Sublime Text (or just open a `.json` file).

You should see a short welcome message on first load.

### Package Control

Pending review on Package Control.

## Usage

1. Open any `.json` file.
2. Place the cursor on a key or inside a value (or select a region).
3. Right-click → **Copy JSON Reference**
   *(the item appears in the clipboard section of the context menu)*
4. The path is copied and a confirmation appears in the status bar.

You can also run **Copy JSON Reference** from the Command Palette.

### Examples

Given this JSON:

```json
{
  "body": {
    "data": {
      "values": {
        "contact": "alice@example.com"
      },
      "items": [
        { "id": 1, "name": "first" }
      ]
    }
  }
}
```

| Cursor position              | Copied path                      |
|-----------------------------|----------------------------------|
| on `"contact"`              | `body.data.values.contact`       |
| on the email value          | `body.data.values.contact`       |
| on `"items"`                | `body.data.items`                |
| on `"name"` inside the array| `body.data.items[0].name`        |

### Settings

Open **Preferences → Package Settings → CopyJSONReference → Settings**,
or run **Preferences: CopyJSONReference Settings** from the Command Palette.
This opens the default and user settings side by side.

```json
{
    // Prepend a leading dot (jq-style). Default: false
    "leading_dot": false,

    // Separator used when multiple selections are copied. Default: newline
    "multi_separator": "\n"
}
```

## Keyboard Shortcut

No key binding is enabled by default, so the package will not conflict with
other shortcuts.

To add one, open **Preferences → Key Bindings** and copy this example into
your user keymap (it is also in `Default.sublime-keymap`):

```json
{
    "keys": ["ctrl+alt+j"],
    "command": "copy_json_reference",
    "context": [
        { "key": "selector", "operator": "equal", "operand": "source.json" }
    ]
}
```

The example is active only inside JSON files. You can use any key combination
you prefer.

## License

MIT — see [LICENSE](LICENSE).

---

**Cold Rock Software**
*Making everyday developer tools a little more pleasant.*
