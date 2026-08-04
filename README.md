# devenv

Personal dev environment as submodules.

bin holds symlinks only.

`scripts/symlinks.py` is the registry of every symlink pointing into this repo;
`scripts/setup` creates them, and `scripts/find-symlinks` audits the registry
against the filesystem (macOS has no reverse symlink index, so it walks the
directories the registry already knows about) and reports links that are missing
from the registry, entries that disagree with disk, and repo config nothing links
to.

