commit:
	git commit -am "Commit"
	git push origin master

pull:
	git reset --HEAD
	git pull origin master

test:
	python laplacek-test.py

clean:
	@-rm -rf __pycache__
	@-rm -rf Icon*
	@-rm -rf *~
