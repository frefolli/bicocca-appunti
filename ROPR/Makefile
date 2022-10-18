@all: double

double:
	pdflatex appunti.tex && pdflatex appunti.tex

single:
	pdflatex appunti.tex && pdflatex appunti.tex

clean:
	export THING="$$(pwd)" && cd ../ && ./cleanlocal.sh "$$THING"
