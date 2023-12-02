assemble:
	mkdir -p build
	cp -r latex build/
	cp -r img build/img
	[ -e build/latex/img ] || ln -s ../img build/latex/img
	#cp -r html5 build/
	#cp -r sphinx build/
	#cp -r docbook build/
	#cp -r sphinx-vimm build/
	#jupyter execute 05-vimm-odt2tei.ipynb
	# jupyter execute web2tei.ipynb
	cp mctb2.tei build/mctb2.tei # for online access
	jupyter execute 10-assemble-TEI.mctb2-only.ipynb

mctb2:
	cd build/latex && latexmk mctb2.tex && plastex -c plastex-mctb2.ini mctb2.tex
	#make -C build/sphinx-vimm html singlehtml epub
	#weasyprint -s html5/style.A4.css build/html5/vimm.html build/html5/vimm.weasyprint.pdf
	#vivliostyle build --style build/html5/style.A4.css --single-doc --timeout 1200 --output build/html5/vimm.vivliostyle.pdf build/html5/vimm.html


