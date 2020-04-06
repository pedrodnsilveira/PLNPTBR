#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
from Helpers import FuncoesAuxiliares

#arquivo PDF para texto
def PDFReader(PDFpath):
    from PDFReader import MyParser

    pdfArray = MyParser(PDFpath)

    pdfText=''
    for linha in pdfArray.records:
            pdfText  = pdfText + linha.decode('utf-8') + ' '

    return pdfText

#extrair sinonimos
def get_Synonym(word):
    from Synonym import MySyn
    S = MySyn()
    return S.get_sinonimos(word)

#extrair palavras-chave
def Extract_KW(nKW,text):
    from KeyWordsPTBR import TextRank4Keyword

    tr4w = TextRank4Keyword()
    text = tr4w.pre_process(text)
    tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
    KW = tr4w.get_keywords(nKW)
    return KW

def PLNTest(corpus,funcao):
    from PLN import PLNPTBR

    pln = PLNPTBR()
    if funcao == 'synonymming': newCorpus = pln.synonymming(corpus)
    elif funcao == 'lemming': newCorpus = pln.lemming(corpus)
    elif funcao == 'stemming': newCorpus = pln.stemming(corpus)
    elif funcao == 'singularing': newCorpus = pln.singularing(corpus)
    return newCorpus

def Similarity(corpus,filesNames='',debug=True):
    from Similarity import Similaridade
    s=Similaridade()
    if filesNames == '':
        files=[]
        c = 1
        for i in range(1,len(corpus)+1):
            files+=str(i)
    else: files = filesNames
    s.get_similarity(corpus,files,debug)

#print PDFReader('PDFFolder/1.pdf')

#print get_Synonym('amor')

'''
import io
with io.open('TXTFolder/a5.txt', "r", encoding="utf-8") as my_file:
    text = my_file.read() 

    a=Extract_KW(10,text)
    for w in a:
        print w
'''
'''
corpus=[['canções','cantor','pagode','utilidade','patife','amor'],
['música','pagode','cachorro','utilidade','amor','cantor'],
['romance','casa','estrutura','legado','legal','amor'],
['nada', 'canção', 'esse', 'texto', 'comércio', 'saudade']]

fa.print_corpus(PLNTest(corpus,'lemming'))
'''

'''
corpus=[['canções','cantor','pagode','utilidade','patife','amor'],
['música','pagode','cachorro','utilidade','amor','cantor'],
['romance','casa','estrutura','legado','legal','amor'],
['nada', 'canção', 'esse', 'texto', 'comércio', 'saudade']]
Similarity(corpus)
'''

'''
fa = FuncoesAuxiliares()
fa.print_corpus(fa.TextFilesKWtoCorpus('TXTFolder',10))
'''

'''
fa = FuncoesAuxiliares()
fa.print_corpus(fa.PDFFileKWtoCorpus('PDFFolder',10))
'''

fa = FuncoesAuxiliares()
r = fa.PDFFileKWtoCorpus('PDFFolder',10)

files = r[0]
corpus = r[1]

from Similarity import Similaridade
s=Similaridade()
s.get_similarity(corpus,files,synonymmingFunction=True,debug=True)
