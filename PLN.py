#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import nltk
import spacy
nlp = spacy.load('pt_core_news_sm')
from Helpers import FuncoesAuxiliares
fa = FuncoesAuxiliares()
class PLNPTBR():
        def synonymming(self,corpus):
                from Synonym import MySyn
                S = MySyn()

                corpusArray,corpusArrayIdx = fa.split_corpus(corpus)

                corpusArrayAux=corpusArray
                for i in range(len(corpusArray)):
                        sinonimos = S.get_sinonimos(corpusArray[i])
                        for sinonimo in sinonimos:
                                for j in range(len(corpusArrayAux)):
                                        if (corpusArray[i] != corpusArrayAux[j]) and (i != j) and (sinonimo == corpusArrayAux[j]):
                                                corpusArray[j]=corpusArray[i]

                corpus = fa.join_corpus(corpusArray, corpusArrayIdx)
                return corpus

        def lemming(self,corpus):
                corpusArray,corpusArrayIdx = fa.split_corpus(corpus)
                
                corpusArrayAux=[]
                corpusText = fa.arrayToString(corpusArray)
                doc = nlp(corpusText)
                tokens = [token for token in doc]
                for token in tokens:
                        corpusArrayAux.append(token.lemma_)

                corpus = fa.join_corpus(corpusArrayAux, corpusArrayIdx)
                return corpus

        def stemming(self,corpus):
                p = nltk.PorterStemmer()
                corpusArray,corpusArrayIdx = fa.split_corpus(corpus)
                
                corpusArrayAux=[]
                for word in corpusArray:
                        #corpusArrayAux.append(stemmer.stem(word))
                        corpusArrayAux.append(p.stem(word))

                corpus = fa.join_corpus(corpusArrayAux, corpusArrayIdx)
                return corpus

        def singularing(self,corpus):

                corpusArray,corpusArrayIdx = fa.split_corpus(corpus)
                corpusArrayAux=[]
                exceptions=['lápis','atlas','pires','ônibus','vírus','paris','seis','dezesseis','tocantins']
                for word in corpusArray:
                        if word not in exceptions:
                                if word[-3:]=='res': word = word[:-3] + 'r'
                                elif word[-3:]=='zes': word = word[:-3] + 'z'
                                elif word[-3:]=='ses': word = word[:-3] + 's'
                                elif word[-3:]=='ões': word = word[:-3] + 'ão'
                                elif word[-3:]=='ãos': word = word[:-3] + 'ão'
                                elif word[-3:]=='ães': word = word[:-3] + 'ão'
                                elif word[-3:]=='ais': word = word[:-3] + 'al'
                                elif word[-3:]=='éis': word = word[:-3] + 'el'
                                elif word[-3:]=='eis': word = word[:-3] + 'il'
                                elif word[-3:]=='óis': word = word[:-3] + 'ol'
                                elif word[-3:]=='uis': word = word[:-3] + 'ul'
                                elif word[-2:]=='as': word = word[:-2] + 'a'
                                elif word[-2:]=='es': word = word[:-2] + 'e'
                                elif word[-2:]=='is': word = word[:-2] + 'i'
                                elif word[-2:]=='os': word = word[:-2] + 'o'
                                elif word[-2:]=='us': word = word[:-2] + 'u'
                                elif word[-2:]=='ns': word = word[:-2] + 'm'

                        corpusArrayAux.append(word)


                corpus = fa.join_corpus(corpusArrayAux, corpusArrayIdx)
                return corpus
