make :
	gcc -o test ~/Desktop/find_root/src/roots.c -I ~/Desktop/gsl/gsl-2.7.1/doc/examples/ -I ~/Desktop/gsl/gsl-2.7.1/ -L /usr/lib -lgsl -lgslcblas
	./test
report : ~/Desktop/find_root/doc/report.tex
	xelatex ~/Desktop/find_root/doc/report.tex
	evince report.pdf





