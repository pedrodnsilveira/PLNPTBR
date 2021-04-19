#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

class RG():

    def getPapers(queryString):

        url = "https://www.researchgate.net/search/publication?q=" + queryString.replace(' ','%20')

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        artigosLinks = soup.findAll(attrs={'class':'nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare'})
        artigosLinks = artigosLinks[:-5]

        artigos = []
        for artigo in artigosLinks:
            if artigo.get_text() != "Source":
                link = artigo.get('href').split("?_sg=")[0]
                artigos += [artigo.get_text() + '|' + 'https://www.researchgate.net/' + link]
        
        return artigos
        #for a in artigos:
        #    print a.encode('utf-8')
