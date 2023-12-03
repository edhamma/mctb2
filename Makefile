default: assemble mctb2

assemble:
	mkdir -p build
	cp -r latex build/
	cp -r img build/img
	[ -e build/latex/img ] || ln -s ../img build/latex/img
	#cp -r html5 build/
	cp -r sphinx-mctb2 build/
	[ -e build/sphinx-mctb2/source/img ] || ln -s ../../img build/sphinx-mctb2/source/img
	#cp -r docbook build/
	#cp -r sphinx-vimm build/
	#jupyter execute 05-vimm-odt2tei.ipynb
	# jupyter execute web2tei.ipynb
	cp mctb2.tei build/mctb2.tei # for online access
	# jupyter execute 10-assemble-TEI.mctb2-only.ipynb
	python3 tei-export.py

mctb2:
	#cd build/latex && latexmk mctb2.tex
	#cd build/latex && plastex -c plastex-mctb2.ini mctb2.tex
	make -C build/sphinx-mctb2 html singlehtml epub
	#weasyprint -s html5/style.A4.css build/html5/vimm.html build/html5/vimm.weasyprint.pdf
	#vivliostyle build --style build/html5/style.A4.css --single-doc --timeout 1200 --output build/html5/vimm.vivliostyle.pdf build/html5/vimm.html


