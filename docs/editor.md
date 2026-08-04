## Editor: VSCode vs Cursor

The environment is currently configured for **VSCode**. Editor identity is
encoded in a few different layers; only two of them are driven by a single
switch today, so flipping back to Cursor is *not* yet a one-liner.

### What controls the editor

1. **CLI launches — one symlink.** `bin/code` is a symlink to the editor's CLI.
   `EDITOR`/`GIT_EDITOR` (`code --wait`) and `OPEN_IN_EDITOR` (`~/bin/code`) all
   funnel through it, so re-pointing this symlink switches every CLI-based open
   at once. This was the intended easy-switch mechanism.
   - VSCode: `/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code`
   - Cursor: `~/.local/bin/cursor`

   `~/bin/code` is the only `code` on `PATH`, so nothing competes with it. Its
   git-committed target is VSCode; during the Cursor years it was manually
   pointed at `~/.local/bin/cursor` and left uncommitted. Just keep `~/bin`
   ahead of any `code` an editor might later install under `/usr/local/bin`.

2. **Wormhole — one env var.** `WORMHOLE_EDITOR` (`shell/env.sh`) drives
   wormhole's CLI, `://` scheme, app-focus name, and extension-install dir.
   Values: `code`, `code-insiders`, `cursor`. (Wormhole's embedded panel always
   uses VSCode `serve-web`, which Cursor does not support — independent of this.)

3. **URL-scheme emitters — hardcoded.** These emit `vscode://` (Cursor uses
   `cursor://`) and are *not* yet variabilised:
   - `shell/env.sh` — `HYPERLINKED_SCHEME` (this one *is* a var)
   - `shell/alias.sh` — the `e` (magit) alias
   - `shell/lib.sh` — `fdd`
   - `tools/bash/rg-delta`
   - `emacs/lib.el` — `dan/open-in-vscode`

4. **GUI app/process targeting — hardcoded.** Reference the app by name/path:
   - `dotfiles/hammerspoon/init.lua` — f17 toggle (`find("Code")`, `Visual Studio Code.app`)
   - `tools/bash/vscode-close-project` — AppleScript `process "Code"`
   - `tools/bash/vscode-summary` — osquery `%Code Helper%`, hs `name() == "Code"`

5. **Settings/keybindings symlinks.** `scripts/symlinks.py` and
   `dotfiles/vscode/create-symlinks` link
   `dotfiles/vscode/{settings,keybindings}.json` into the `Code`,
   `Code - Insiders` and `Cursor` support dirs. Harmless either way: each editor
   ignores the others' directory.

### To switch back to Cursor

1. `ln -sfn ~/.local/bin/cursor bin/code`
2. In `shell/env.sh`: `WORMHOLE_EDITOR=cursor`, `HYPERLINKED_SCHEME=cursor`;
   re-`source` and restart the wormhole server.
3. Replace `vscode://` → `cursor://` in the four emitters under (3) above.
4. In the three files under (4): `Cursor` / `/Applications/Cursor.app` /
   `%cursor%` / `name() == "Cursor"`.
5. Nothing to do: the Cursor `User` links are already in place.
6. Reload Hammerspoon; reinstall the wormhole extension into Cursor
   (`WORMHOLE_EDITOR=cursor make -C ~/src/wormhole/vscode-extension install`).

### How close is on-demand switching?

Layers 1 and 2 are single-switch. Layers 3–5 are hardcoded across zsh, lua,
AppleScript, and elisp — ~10 sites, so today a full switch is a manual edit pass
(steps 3–5), not a flag flip.

To make it on-demand, introduce one source of truth that every layer reads:

- **Scheme (3)** is the cheap win: `HYPERLINKED_SCHEME` already exists — have the
  `e` alias, `fdd`, `rg-delta`, and `lib.el` read it instead of hardcoding.
- **App/process (4)** needs name + `.app` path + CLI derived from the same flavour.
  The obstacle is that Hammerspoon (and AppleScript run from a tool) don't see the
  shell env, so the source of truth should be a small file both can read — e.g.
  `~/.config/editor-flavor` holding `code`|`cursor`, sourced by zsh and read at
  Hammerspoon load. `WORMHOLE_EDITOR` could be derived from it for consistency.

With that file in place, switching becomes: write the file, reload shell +
Hammerspoon. The settings-symlink layer (5) can stay pointed at both editors'
dirs permanently, since each editor ignores the other's directory.
