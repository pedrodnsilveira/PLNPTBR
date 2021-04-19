#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re

class YT():

    def getVideos(queryString):

        url = "https://www.youtube.com/results?search_query=" + queryString.replace(' ','+')

        response = requests.get(url)
        html = response.text

        ScraperAllIds = [m.start() for m in re.finditer('title":{"runs"', html)]
            videos = []
            urlBase='https://www.youtube.com/watch?v='
            for videoId in ScraperAllIds:
                text = html[videoId-180:videoId+150]
                if "hqdefault.jpg?" in text:
                    v_id = text.split('.com/vi/')[1].split('/hqdefault')[0]
                    title = text.split('[{"text":"')[1].split('"}],"accessibility"')[0]
                    videos += [title.replace('|',' ') + "|" + urlBase + v_id]
        
        return videos
        #for v in videos:
        #    print v.encode('utf-8')
