@all:
	pdflatex appunti.tex

clean:
	find . -name "*.aux" -type f -delete
	find . -name "*.dvi" -type f -delete
	find . -name "*.idx" -type f -delete
	find . -name "*.out" -type f -delete
	find . -name "*.log" -type f -delete
	find . -name "*.ilg" -type f -delete
	find . -name "*.ind" -type f -delete

depclean: clean
	rm -rf *.pdf