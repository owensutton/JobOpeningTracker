#
#
#

import django
import scrapy
import webbrowser
import requests

def googlejobs():
    res = requests.get('https://careers.google.com')
    print(res)



googlejobs()
