# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:46:03 2020

@author: Achraf
"""

import requests
from bs4 import BeautifulSoup

URL = "http://www.instagram.com/{}/"

def scrape(username):
    full_url = URL.format(username) # make full url
    r = requests.get(full_url) # send get request
    s = BeautifulSoup(r.text, "lxml") # make soup obj
    
    tag= s.find("meta", attrs = {"name":"description"})
    text = tag.attrs['content'] # grab the content text
    main_text = text.split("-")[0] # required text
    
    return main_text

USERNAME = "achrafzbaida"
data = scrape(USERNAME)
print(data) 