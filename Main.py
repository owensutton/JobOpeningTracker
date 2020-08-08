#
#
#

import django
import scrapy
import webbrowser
from bs4 import BeautifulSoup
from lxml import html
import requests
import selenium


def googlejobs():

    # Start Scraping google career website
    print ('Scraping Google Career Website')

    # get the page request
    url = "https://careers.google.com/jobs/results/?company=Google&company=YouTube&company=Google%20Fiber&employment_type=FULL_TIME&hl=en_US&jlo=en_US&q=&sort_by=relevance"
    page = requests.get(url)

    # Parse request into html
    soup = BeautifulSoup(page.text)


    #Get job titles
   # title = tree.xpath('//div[@class="gc-h-unstyled-list gc-p-results__results-list"]/text()')
    title = tree.xpath('//div/h1/p/a/span[@class="gc-h-hidden--until-medium"]/text()')
    print 'Title: ', title


def ArtisanPartnerJobs():

    print('Scraping Artisan PartnerJobs')

    url = 'https://www.artisanpartners.com/careers/career-opportunities.html'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    title = soup.find_all('title')
    print title

    h1 = soup.find('h1')
    print h1



ArtisanPartnerJobs()
