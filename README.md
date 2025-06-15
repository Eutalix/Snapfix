# Snapfix

🇧🇷 [Leia esta documentação em português](./README.pt.md)

Snapfix is a tool for automatically organizing Snap application `.desktop` entries in the user's application menu.

---

## Overview

* **What it does**: Detects installed snaps, creates/updates `.desktop` files in `~/.local/share/applications/`, fixes categories, resolves icons, and adds an uninstall action via Polkit (`pkexec snap remove`).
* **Distribution**: Provided as a downloadable standalone binary in GitHub Releases.
* **Goal**: Allow Linux Mint users to automatically organize Snap applications.

---

## Binary Download

1. Download with:

   ```bash
   wget "https://github.com/Eutalix/Snapfix/releases/download/v1.0/snapfix"
   ```

   or download the file from the [Releases](https://github.com/Eutalix/Snapfix/releases/) page.

2. Save the file in a directory of your choice, e.g., `~/snapfix` or `~/bin`.

---

## Make It Executable

After downloading, make the file executable:

```bash
chmod +x ~/snapfix
```

---

## Add to PATH via bashrc (optional)

To make it easier to run, you can add the binary's directory to your `PATH` by editing `~/.bashrc` (or `~/.zshrc`, depending on your shell). For example, if you saved it to `~/snapfix`, add:

```bash
# Snapfix
export PATH="$HOME/snapfix:$PATH"
```

Or, if you renamed and saved it to `~/bin` as `snapfix`:

```bash
# Snapfix
export PATH="$HOME/bin:$PATH"
```

After editing, reload bashrc:

```bash
source ~/.bashrc
```

### Automatically Add via Command

Alternatively, use a single command to append to the end of your `~/.bashrc`. For example, if the binary is in `~/snapfix`:

```bash
echo 'export PATH="$HOME/snapfix:$PATH"' >> ~/.bashrc
```

Or, if it’s in `~/bin/snapfix`:

```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
```

Then reload:

```bash
source ~/.bashrc
```

Now you can run `snapfix` from anywhere:

```bash
snapfix --help
```

---

## Basic Execution

Open a terminal and run the binary directly:

* `--auto`: runs in a continuous loop (default interval is 300s).
* `--force`: forces recreation of existing entries.
* `--debug`: detailed logging.
* `--background`: runs in background (`--auto` in subprocess).
* `--autostart`: enables auto-run on system startup (creates file in `~/.config/autostart`).
* `--version`: shows version info.

### Examples

* **Help**:

  ```bash
  ~/snapfix --help
  ```

  Shows usage instructions.

* **Run once (manual)**:

  ```bash
  ~/snapfix
  ```

  Updates/creates `.desktop` entries for currently installed snaps.

* **Run with debug**:

  ```bash
  ~/snapfix --debug
  ```

  Shows logs including processed snaps, resolved icons, skipped entries, etc.

* **Force recreation**:

  ```bash
  ~/snapfix --force
  ```

  Recreates all entries, even if they already exist.

* **Continuous mode**:

  ```bash
  ~/snapfix --auto
  ```

  Runs repeatedly at fixed intervals (default: 300 seconds).

* **Background mode**:

  ```bash
  ~/snapfix --background
  ```

  Returns to terminal and continues running in the background.

* **Enable autostart**:

  ```bash
  ~/snapfix --autostart
  ```

  On next login, Snapfix will auto-start in background.

---

## Optional Configuration

Although the binary works with default settings, you can use a JSON config file in `~/.config/snapfix/config.json` to customize filters and intervals:

### Example `~/.config/snapfix/config.json`

```json
{
  "skip_patterns": ["url-handler", "show-updates"],
  "skip_name_patterns": ["Show Updates", "URL Handler"],
  "freedesktop_categories": {"CustomRaw": "Utility"},
  "mapping": {"CustomRaw": "Utility"},
  "loop_interval": 600
}
```

* Create the folder if it doesn't exist:

  ```bash
  mkdir -p ~/.config/snapfix
  ```

* Edit or create the JSON file with your preferred options.

* Run the binary normally — it will detect and load this config.

* To use a config file from another location, use the `--config` flag:

  ```bash
  ~/snapfix --config /path/to/other/config.json
  ```

---

## Menu Integration

* After running Snapfix, `.desktop` entries are created in `~/.local/share/applications/`.
* Open your application menu (e.g., GNOME, KDE, Cinnamon) and check if Snap apps appear correctly with icons and categories.
* To uninstall an app via the menu, right-click the icon and use the added “Uninstall” action. If it's not shown, use the terminal: `snap remove <snap_name>`.

---

## Full Removal

* To stop continuous execution: kill the background process (`ps aux | grep snapfix`, then `kill <pid>`).

* To remove the config:

  ```bash
  rm -rf ~/.config/snapfix
  ```

* To delete created `.desktop` entries, manually remove files in `~/.local/share/applications/` starting with unwanted snap names.

* To remove the binary: delete the executable file from `~/` or wherever it was saved.

---

## Contact & Support

* For bugs or questions, visit the [Issues](https://github.com/Eutalix/Snapfix/issues) page.
