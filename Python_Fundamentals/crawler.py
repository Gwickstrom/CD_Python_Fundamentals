# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
pp = pprint.PrettyPrinter()

url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url))
print soup # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below

def print_links(url):
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    links = soup.findAll('a', href=True)
    #recursive = True
    list_of_links = []
    for link in links:
        if link not in list_of_links:
            list_of_links.append(str(link['href']))
    pp.pprint(list_of_links)

print_links(url)

def print_all_links(url):
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    links = soup.findAll('a', href=True)
    dict_of_links = {}
    for link in links:
        if str(link['href']) in dict_of_links:
            dict_of_links[str(link['href'])] +=1
        else:
            dict_of_links[str(link['href'])] = 1
        pp.pprint(dict_of_links)

print_all_links(url)