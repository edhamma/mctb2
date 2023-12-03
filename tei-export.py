#!/usr/bin/python3
import sys
import os
from lxml import etree
sys.path.append('.')
import tei_exporters

mctbTEI=etree.parse('mctb2.tei',etree.XMLParser(remove_comments=True)).getroot() 

if 1:
    latexWriter=tei_exporters.LatexWriter()
    for e in mctbTEI.iter():
        if e.tag=='emph': e.tag='em'
    for e in mctbTEI.findall('.//body'): e.tag='main'
    for l in mctbTEI.findall('.//list'):
        if 'rend' in l.attrib: l.attrib['type']=l.attrib['rend']
        if 'style' in l.attrib:
            l.attrib['subtype']=l.attrib['style']
            #if s=='1': l.attrib['subtype']='1)'
            # l.attrib['subtype']=s+'.'
    for n in mctbTEI.findall('.//note'): n.attrib['n']='X'
    for t in mctbTEI.findall('.//table'): t.attrib['rend']='ceylon'
    print('MCTB2')
    open('build/latex/mctb2-body.tex','w').write(latexWriter.write(mctbTEI))

if 1:
    # sphinx
    os.makedirs('build/sphinx-mctb2/source',exist_ok=True)
    sphinxWriter=tei_exporters.SphinxWriter(outdir='build/sphinx-mctb2/source',vimm=True,chapters_arabic=True)
    # mctbTEI=etree.parse('mctb2.tei',etree.XMLParser(remove_comments=True)).getroot() 
    sphinxWriter.write(mctbTEI)
    sphinxWriter.writeIndex(title='Mastering the Core Teachings of the Buddha')
