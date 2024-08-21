diff:
	git submodule foreach git diff HEAD

push:
	git submodule foreach git push -f origin HEAD:main
	git commit -am '🧬'
	git push

