#!/usr/bin/env python
# coding: utf-8

from PLN import PLNPTBR
from sklearn.feature_extraction.text import TfidfVectorizer
from Auxiliar import FuncoesAuxiliares

class Similaridade():

        #####calcular similaridade
        def get_similarity(self,corpus,files,print_result=True,singularingFunction=True,synonymmingFunction=True,stemmingFunction=False,lemmingFunction=False,debug=False):
                pln = PLNPTBR()
                fa = FuncoesAuxiliares()
                if(debug): print ("corpus original:")
                if(debug): fa.print_corpus(corpus)
                
                #Plural para singular
                #Funciona bem, mas apresenta alguns erros
                if singularingFunction:
                        corpus = pln.singularing(corpus)
                        if(debug): print ("corpus considerando singularing:")
                        if(debug): fa.print_corpus(corpus)

                #Passa a considerar sinonimos no calculo de similaridade. 
                #Aumenta consideravelmente o tempo de execução.
                #melhora muito o cálculo
                if synonymmingFunction:
                        corpus = pln.synonymming(corpus)
                        if(debug): print ("corpus considerando sinonimos:")
                        if(debug): fa.print_corpus(corpus)

                #Passa a considerar o radical da palavra
                #Não funciona muito bem para portugues
                if stemmingFunction:
                        corpus = pln.stemming(corpus)
                        if(debug): print ("corpus considerando stemming:")
                        if(debug): fa.print_corpus(corpus)

                #Passa a considerar o lema da palavra
                #Não funciona muito bem para portugues
                if lemmingFunction:
                        corpus = pln.lemming(corpus)
                        if(debug): print ("corpus considerando lemming:")
                        if(debug): fa.print_corpus(corpus)
                
                corpusText = []
                for ca in corpus:
                        FileKWtext = fa.arrayToString(ca)
                        corpusText.append(FileKWtext)

                vect = TfidfVectorizer(min_df=1)
                tfidf = vect.fit_transform(corpusText) #each sentence can be replaced by a whole document

                MS = (tfidf * tfidf.T).A #similarities matrix of sentences
                if print_result:
                        import pandas as pd
                        df = pd.DataFrame(MS, columns=files, index=files)
                        print df