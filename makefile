main :   
	cd source && python main.py
	jupyter nbconvert --to html source/130010024.ipynb
	mv source/130010024.html output/
	make paper

paper: 
	cp source/bib_file.bib . 
	pdflatex -output-directory output source/130010024.tex 
	bibtex output/130010024.aux
	pdflatex -output-directory output source/130010024.tex
	pdflatex -output-directory output source/130010024.tex
	rm bib_file.bib

.PHONY: clean tests

test:
	pytest source/spring_mass_damper.py
clean:	 
	rm -rf output
	rm -rf source/__pycache__
