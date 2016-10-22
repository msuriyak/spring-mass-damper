FILES := Paper.pdf 
AUXFILES := $(FILES:.pdf=.aux)
LOGFILES := $(FILES:.pdf=.log)
BBLFILES := $(FILES:.pdf=.bbl)
BLGFILES := $(FILES:.pdf=.blg)
PICS := $(wildcard *.png)
PICSDEL := $(filter-out spring_mass_damper.png,$(PICS))
PYC := $(wildcard *.pyc)

main : ../source/spring_mass_damper.py ../source/main.py
	python main.py
	make pdf

pdf : $(FILES:.pdf=.tex) 
	make Paper.pdf

%.pdf: %.tex 
	pdflatex -output-directory ../output $< 
	bibtex ../output/`echo $< |cut -d "." -f1`.aux
	pdflatex -output-directory ../output $<
	pdflatex -output-directory ../output $<

.PHONY: clean clean-all
clean-all:
	$(RM) $(AUXFILES) $(FILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) $(OTHERS) $(PICSDEL) $(PYC)

clean:	 
	$(RM) $(AUXFILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) $(OTHERS) $(PICSDEL) $(PYC)

