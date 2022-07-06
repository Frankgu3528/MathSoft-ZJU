report : final.tex 
	xelatex final.tex
	bibtex final
	xelatex final.tex
	xelatex final.tex

clean :
	rm slide.nav
	rm slide.out
	rm slide.snm
	rm slide.aux
	rm slide.log
	rm slide.toc
	rm final.aux
	rm final.log
	rm final.bbl
	rm final.blg
slide : slide.tex 
	xelatex slide.tex
	xelatex slide.tex
	evince slide.pdf
