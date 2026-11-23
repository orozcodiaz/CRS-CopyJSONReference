# CRS - Copy JSON Reference

**Copy the JSON path of the node under your cursor with a single right-click.**

Right-click any key or value inside a JSON file and choose **CRS - Copy JSON Reference**.  
The dotted path (e.g. `body.data.values.contact`) is instantly copied to the clipboard.

Created by **Cold Rock Software**.

---

## Features

- Context menu item that appears next to the regular **Copy** action
- Command Palette entry: `CRS - Copy JSON Reference`
- Keyboard shortcut: `Ctrl+Alt+J` (only active in JSON files)
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
3. Extract the `CRS-CopyJSONReference` folder into the Packages directory.
4. Restart Sublime Text (or just open a `.json` file).

You should see a short welcome message on first load.

### Package Control

(Not yet published — coming soon if there is demand.)

## Usage

1. Open any `.json` file.
2. Place the cursor on a key or inside a value (or select a region).
3. Right-click → **CRS - Copy JSON Reference**  
   *(the item appears in the clipboard section of the context menu)*
4. The path is copied and a confirmation appears in the status bar.

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

Open **Preferences → Package Settings → CRS - Copy JSON Reference → Settings**  
(or edit `CRS-CopyJSONReference.sublime-settings`):

```json
{
    // Prepend a leading dot (jq-style). Default: false
    "leading_dot": false,

    // Separator used when multiple selections are copied. Default: newline
    "multi_separator": "\n"
}
```

## Keyboard Shortcut

Default binding (active only inside JSON):

| Platform     | Shortcut     |
|--------------|--------------|
| Windows/Linux| `Ctrl+Alt+J` |
| macOS        | `Ctrl+Alt+J` |

You can override it in your user key bindings.

## License

MIT — see [LICENSE](LICENSE).

---

**Cold Rock Software**  
*Making everyday developer tools a little more pleasant.*
