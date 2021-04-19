#!/usr/bin/env python
# coding: utf-8
import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from StringIO import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
import os
 
class MyParser(object):
    def __init__(self, pdf):
        ## Snipped adapted from Yusuke Shinyamas 
        #PDFMiner documentation
        # Create the document model from the file
        parser = PDFParser(open(pdf, 'rb'))
        document = PDFDocument(parser)
        # Try to parse the document
        # Quebra a criptografia de arquivos pdf "travados". 
        # Está comentado pois só funciona para Linux.
        '''
        if not document.is_extractable:
            #print pdf
            #raise PDFTextExtractionNotAllowed
            newPDF=pdf.replace('.pdf','_dec.pdf')
            bashCmd = 'qpdf --decrypt ' + pdf + ' ' + newPDF
            os.system(bashCmd)
            #bashCmd = 'mv ' + ' dec_' + pdf + ' ' + pdf
            #os.system(bashCmd)
            parser = PDFParser(open(newPDF, 'rb'))
            document = PDFDocument(parser)
            os.remove(newPDF)
        '''
        # Create a PDF resource manager object 
        # that stores shared resources.
        rsrcmgr = PDFResourceManager()
        # Create a buffer for the parsed text
        retstr = StringIO()
        # Spacing parameters for parsing
        laparams = LAParams()
        codec = 'utf-8'
 
        # Create a PDF device object
        device = TextConverter(rsrcmgr, retstr, 
                               codec = codec, 
                               laparams = laparams)
        # Create a PDF interpreter object
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
         
        self.records            = []
         
        lines = retstr.getvalue().splitlines()
        for line in lines:
            self.handle_line(line)
     
    def handle_line(self, line):
        # Customize your line-by-line parser here
        self.records.append(line)

''' 
if __name__ == '__main__':
    p = MyParser(sys.argv[1])
    print '\n'.join(p.records)


corpus = [['pessoa', 'vida', 'estrada', 'netto'], ['estrada', 'coisas', 'pessoas', 'vida', 'david'], ['pessoas', 'estrada', 'mundo'], ['raiva']]
print corpus
corpus = singularing(corpus)
print corpus
'''