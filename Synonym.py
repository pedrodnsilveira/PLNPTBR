#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
#from unicodedata import normalize

class MySyn():

    def get_sinonimos(self,queryword):

        #queryword = normalize('NFKD', queryword.decode('utf-8')).encode('ASCII', 'ignore')

        r = requests.get('http://www.lexico.pt/' + queryword)
        
        soup = BeautifulSoup(r.text, "lxml")

        try:
            listinha = soup.find("p", class_="text words-buttons").text.strip()
        except AttributeError:
            # 404 ou não tem sinónimos
            return []

        palavras = listinha.split(", ")
        return palavras