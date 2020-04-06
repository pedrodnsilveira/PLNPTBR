#!/usr/bin/env python
# coding: utf-8
import io
from os import listdir
from os.path import isfile, join

class FuncoesAuxiliares():

        def split_corpus(self,corpus):
                corpusArray=[]
                corpusArrayIdx=[]
                for sentence in corpus:
                        idx = 0
                        for word in sentence:
                                corpusArray.append(word)
                                idx = idx + 1
                        corpusArrayIdx.append(idx)
                return corpusArray, corpusArrayIdx

        def join_corpus(self,corpusArray, corpusArrayIdx):
                corpus=[]
                arr=[]
                i=0
                count=0
                for word in corpusArray:
                        arr.append(word)
                        count = count + 1
                        if count == corpusArrayIdx[i]:
                                corpus.append(arr)
                                i = i + 1
                                count = 0
                                arr=[]
                return corpus

        def print_corpus(self,corpus):
                for arr in corpus:
                        for element in arr:
                                print element + ' ',
                        print('')
                print('**')

        def arrayToString(self,arr):
                strr = ''
                for w in arr:
                        strr = strr + w + ' '
                return strr[:-1]

        #extrair palavras-chave
        def Extract_KW(self,nKW,text):
                from KeyWordsPTBR import TextRank4Keyword

                tr4w = TextRank4Keyword()
                text = tr4w.pre_process(text)
                tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
                KW = tr4w.get_keywords(nKW)
                return KW

        def FilesNamesToArray(self,path):
                files = [f for f in listdir(path) if isfile(join(path, f))]
                return files

        def TextFilesKWtoCorpus(self,path,nKW):
                corpus = []
                files = [f for f in listdir(path) if isfile(join(path, f))]
                for f in files:
                        f=path+'/'+f
                        with io.open(f, "r", encoding="utf-8") as my_file:
                                text = my_file.read() 

                        fileKW=self.Extract_KW(nKW,text)
                        corpus.append(fileKW)
                return [files,corpus]

        def PDFFileKWtoCorpus(self,path,nKW):
                from PDFReader import MyParser

                #lê a pasta de arquivos PDF e pega o nome de cada um dos arquivos e preenche o vetor
                files = [f for f in listdir(path) if isfile(join(path, f))]

                corpus = []
                for f in files:
                        print path+'/'+f
                        pdfArray = MyParser(path+'/'+f)
                        pdfText=''
                        for linha in pdfArray.records:
                                pdfText  = pdfText + linha.decode('utf-8') + ' '

                        fileKW=self.Extract_KW(nKW,pdfText)
                        corpus.append(fileKW)
                return [files,corpus]