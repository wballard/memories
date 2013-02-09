DIFF = git --no-pager diff --ignore-all-space --color-words --no-index

install:
	./setup.py install

test: install
	-rm test/.testdb test/.new
	cat test/remember_these | memories remember test/.testdb
	cat test/check_these | memories new test/.testdb > test/.new
	$(DIFF) test/expect_these test/.new
	cat test/check_these | memories forget test/.testdb
	cat test/check_these | memories new test/.testdb > test/.new
	$(DIFF) test/check_these test/.new
