"""Registry of every symlink pointing into this repo.

Sources are absolute or ~-relative; targets are repo-relative unless they start
with ~.
"""

from pathlib import Path

devenv = Path(__file__).parents[1].resolve()

symlinks = [
    ("/Applications/Alacritty.app", "~/src/alacritty/target/release/osx/Alacritty.app"),
    ("/Applications/Wormhole.app", "~/src/wormhole/gui/dist/Wormhole/Wormhole.app"),
    ("~/.agents", "dotfiles/ai/agents"),
    ("~/.alacritty.toml", "dotfiles/alacritty/alacritty.toml"),
    ("~/.claude/settings.json", "dotfiles/ai/claude/claude-code-settings.json"),
    ("~/.claude/skills", "skills"),
    ("~/.codex/AGENTS.md", "temporal/dotfiles/AGENTS.md"),
    ("~/.codex/config.toml", "dotfiles/codex/config.toml"),
    ("~/.config/atuin", "dotfiles/atuin"),
    ("~/.config/gh/config.yml", "dotfiles/gh/config.yml"),
    ("~/.config/gitu", "dotfiles/gitu"),
    ("~/.config/karabiner", "dotfiles/karabiner"),
    ("~/.config/litecli/config", "dotfiles/dbcli/litecli.ini"),
    ("~/.config/micro/bindings.json", "dotfiles/micro/bindings.json"),
    ("~/.config/micro/colorschemes", "dotfiles/micro/colorschemes"),
    ("~/.config/micro/init.lua", "dotfiles/micro/init.lua"),
    ("~/.config/micro/plug", "dotfiles/micro/plug"),
    ("~/.config/micro/settings.json", "dotfiles/micro/settings.json"),
    ("~/.config/uv/uv.toml", "dotfiles/uv/uv.toml"),
    ("~/.config/wormhole", "dotfiles/wormhole"),
    ("~/.cursor/.cursor.0/rules", "dotfiles/ai/cursor/rules"),
    ("~/.cursor/cli-config.json", "dotfiles/ai/cursor/cli-config.json"),
    ("~/.cursor/skills", "skills"),
    ("~/.digrc", "dotfiles/dig/digrc"),
    ("~/.dircolors", "dotfiles/dircolors/dircolors"),
    ("~/.emacs.d/init.el", "emacs/emacs.el"),
    ("~/.finicky.js", "dotfiles/finicky/finicky.js"),
    ("~/.gitconfig", "dotfiles/git/gitconfig"),
    ("~/.hammerspoon/init.lua", "dotfiles/hammerspoon/init.lua"),
    (
        "~/.ipython/profile_default/ipython_config.py",
        "dotfiles/ipython/ipython_config.py",
    ),
    ("~/.kimi-code/tui.toml", "dotfiles/kimi-code/tui.toml"),
    ("~/.lesskey", "dotfiles/less/lesskey"),
    ("~/.local/bin/docker-guard", "dotfiles/macos/docker-guard"),
    ("~/.local/bin/docker-start", "dotfiles/macos/docker-start"),
    ("~/.local/bin/docker-stop", "dotfiles/macos/docker-stop"),
    ("~/.neo/neo.toml", "dotfiles/neomorphus/neomorphus.toml"),
    ("~/.pdbrc.py", "dotfiles/pdb/pdbrc.py"),
    ("~/.pi/agent/models.json", "dotfiles/ai/pi/models.json"),
    ("~/.qwen/settings.json", "dotfiles/ai/qwen/settings.json"),
    ("~/.shellcheckrc", "dotfiles/shellcheck/shellcheckrc"),
    ("~/.tmux.conf", "dotfiles/tmux/tmux.conf"),
    ("~/.zshrc", "shell/init.zsh"),
    ("~/AGENTS.md", "temporal/dotfiles/AGENTS.md"),
    ("~/CLAUDE.md", "temporal/dotfiles/AGENTS.md"),
    ("~/GEMINI.md", "temporal/dotfiles/AGENTS.md"),
    ("~/bin", "bin"),
    ("~/devenv", "~/src/devenv"),
    (
        "~/Library/LaunchAgents/my.clean-login.plist",
        "dotfiles/macos/my.clean-login.plist",
    ),
    (
        "~/Library/LaunchAgents/my.docker-guard.plist",
        "dotfiles/macos/my.docker-guard.plist",
    ),
    (
        "~/Library/Application Support/Claude/claude_desktop_config.json",
        "dotfiles/ai/claude/claude_desktop_config.json",
    ),
    (
        "~/Library/Application Support/Cursor/User/snippets",
        "dotfiles/vscode/snippets",
    ),
    (
        "~/Library/Application Support/FluidVoice/parakeet_custom_vocabulary.json",
        "dotfiles/fluidvoice/parakeet_custom_vocabulary.json",
    ),
    (
        "~/Library/Application Support/Firefox/Profiles/fpe30uji.default-release/chrome/userChrome.css",
        "dotfiles/firefox/userChrome.css",
    ),
    (
        "~/Library/Application Support/Firefox/Profiles/fpe30uji.default-release/chrome/userContent.css",
        "dotfiles/firefox/userContent.css",
    ),
    ("~/Library/Application Support/k9s/config.yml", "dotfiles/k9s/config.yml"),
    ("~/Library/Application Support/k9s/skin.yml", "dotfiles/k9s/skin.yml"),
    ("~/Library/Application Support/xbar/plugins", "dotfiles/xbar"),
    ("~/src/wormhole/.wormhole.toml", "dotfiles/wormhole/wormhole.toml"),
    ("~/src/temporalio/saas-cicd/.vscode", "dotfiles/vscode/workspaces/saas-cicd"),
]

for editor in ["Code", "Code - Insiders", "Cursor"]:
    symlinks.extend(
        [
            (
                f"~/Library/Application Support/{editor}/User/settings.json",
                "dotfiles/vscode/settings.json",
            ),
            (
                f"~/Library/Application Support/{editor}/User/keybindings.json",
                "dotfiles/vscode/keybindings.json",
            ),
        ]
    )


def resolve(source: str, target: str) -> tuple[Path, Path]:
    return (
        Path(source).expanduser(),
        Path(target).expanduser() if target.startswith("~") else devenv / target,
    )
