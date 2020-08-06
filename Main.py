#
#
#

import django
import scrapy
import webbrowser
from lxml import html
import requests

def googlejobs():

    # Start Scraping google career website
    print ('Scraping Google Career Website')
    # get the page request
    page = requests.get('https://careers.google.com/jobs/results/?company=Google&company=YouTube&company=Google%20Fiber&employment_type=FULL_TIME&hl=en_US&jlo=en_US&q=&sort_by=relevance')

    # Parse request into html
    tree = html.fromstring(page.content)

    #Get job titles
    title = tree.xpath('//div[@id="search-results"]/text()')
    print 'Title: ', title



googlejobs()
