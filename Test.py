#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
from Helpers import FuncoesAuxiliares

###########################
# Biliotecas necessárias: #
#      BeautifulSoup      #
#         requests        #
#         sklearn         #
#          spacy          #
#           nltk          #
#         pdfminer        #
#          pandas         #
###########################

#Exemplo de como converter um arquivo PDF para texto
#Parametro: caminho para o arquivo pdf: string
#Retorno: texto do arquivo pdf: string
def PDFReader(PDFpath):
    from PDFReader import MyParser

    pdfArray = MyParser(PDFpath)

    pdfText=''
    for linha in pdfArray.records:
            pdfText  = pdfText + linha.decode('utf-8') + ' '

    return pdfText

#Exemplo de como obter os sinônimos de uma palavra. 
#Necessário estar conectado à internet
#Parâmetro: palavra alvo de sinônimo: string
#Retorno: lista com os sinônimos: Array
def get_Synonym(word):
    from Synonym import MySyn
    S = MySyn()
    return S.get_sinonimos(word)

#Exemplo de como extrair as N palavras-chave de um texto.
#Parâmetro 1: número de palavras-chave a serem extraídas: int
#Parâmetro 2: texto alvo da extração: string
#Retorno: lista de palavras-chave: Array
def Extract_KW(nKW,text):
    from KeyWordsPTBR import TextRank4Keyword

    tr4w = TextRank4Keyword()
    text = tr4w.pre_process(text)
    tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
    KW = tr4w.get_keywords(nKW)
    return KW

#Exemplo de como executar algumas funções de PLN em português.
#Parâmetro 1: conjunto de textos já tokenizados: Array bi-dimensional MxN (matriz).
#    Sugestão que essa função seja usada em conjunto com a de extrair palavras-chave
#    que já traz o texto tokenizado em sua maior carga semântica.
#Parâmetro 2: Valor fixo de uma das quatro funções implementadas:
#    "synonymming": string
#    "lemming": string
#    "stemming": string
#    "singularing": string
#Retorno: lista de palavras-chave: Array
#OBS: Se o corpus for muito grande (por exemplo mais de 20 documentos), fica inviável
#a utilização da função que retorna sinônimos, pois além do processamento de substi-
#tuição dos sinônimos pelo termo (que tem complexidade quadrática O(n²)), tem o pro-
#blema de fazer o scrap para cada token, fazendo acesso externo à internet.
def PLNTest(corpus,funcao):
    from PLN import PLNPTBR

    pln = PLNPTBR()
    if funcao == 'synonymming': newCorpus = pln.synonymming(corpus)
    elif funcao == 'lemming': newCorpus = pln.lemming(corpus)
    elif funcao == 'stemming': newCorpus = pln.stemming(corpus)
    elif funcao == 'singularing': newCorpus = pln.singularing(corpus)
    return newCorpus

#Exemplo de como executar a função de encontro de similaridades entre textos.
#Parâmetro 1: conjunto de textos já tokenizados: Array bi-dimensional MxN (matriz).
#    Sugestão que essa função seja usada em conjunto com a de extrair palavras-chave
#    que já traz o texto tokenizado em sua maior carga semântica.
#Parâmetro 2: nomes dos arquivos (na mesma ordem em que eles estejam no corpus): Array
#Parâmetro 3: impressão dos retornos, passoa-a-passo durante a execução da função: bool
#Retorno: Não está implementado retorno explícito. Apenas a impressão da matriz de si-
#milaridade. Isso pode ser mudado na função "get_similarity" do arquivo "Similarity.py".
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

#Exemplo de como executar o robô de busca por videos no YouTube.
#Parâmetro 1: A chave de busca: String
#Retorno: lista de descrições dos videos e suas respespectivas urls: Array
#OBS: O retorno está separado por "|". Exemplo: [descricaoVideo|urlVideo]
def YTTest(searchQuery):
    from YouTube import YT

    yt = YT()
    videos = yt.getVideos(searchQuery)
    return videos

#Exemplo de como executar o robô de busca por artigos no ResearchGate.
#Parâmetro 1: A chave de busca: String
#Retorno: lista de títulos dos papers e suas respespectivas urls: Array
#OBS: O retorno está separado por "|". Exemplo: [tituloPaper|urlPaper]
def RGTest(searchQuery):
    from ResearchGate import RG

    rg = RG()
    papers = yt.getPapers(searchQuery)
    return papers

#Exemplo de como executar o robô de busca por artigos no Google Scholar
#Tem um grande problema nesta função. O google trava depois de umas duas consultas,
#pois detecta que trata-se de uma consulta automatizada.
#Parâmetro 1: A chave de busca: String
#Retorno: lista de títulos dos papers e suas respespectivas urls: Array
#OBS: O retorno está separado por "|". Exemplo: [tituloPaper|urlPaper]
def ScholarTest(searchQuery):
    pycommand = 'python Scholar.py -c 10 --csv --all ' + '"'+searchQuery+'"'
    response = system_call(pycommand)
    papers = response.split('\n')
    return papers

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
