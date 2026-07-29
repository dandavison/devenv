diff:
	git submodule foreach git diff HEAD

macos-defaults-import:
	./dotfiles/macos/macos-defaults import

push:
	git submodule foreach git push -f origin HEAD:main
	git commit -am '🧬'
	git push

