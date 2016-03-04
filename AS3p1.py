from StringIO import StringIO    
import pycurl
import requests
import certifi
import lynx
import re
from bs4 import BeautifulSoup
import nltk
from urllib import urlopen

i = 0
for line in open('Testfile.txt','r'):
#Name and open Documents*****************
    docnumber = './doc' + str(i) + '.txt'
    prodocnumber = './prodoc' + str(i) + '.txt'
    #print docnumber
    #print prodocnumber
    docs = open(docnumber , 'w+')
    #prodocs = open(prodocnumber , 'w+')
#****************************************

#Get the URL*****************************
    url = str(line)
    url = url[:-1]
#****************************************

#Curl uri to file************************
    storage = StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.CONNECTTIMEOUT, 60)
    c.setopt(pycurl.TIMEOUT, 120)
    c.setopt(pycurl.NOSIGNAL, 30)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.MAXREDIRS, 20)
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, storage.write)
    try:
        c.perform()
        c.close()
        content = storage.getvalue()
        #print content
        docs.write(content)
        docs.close()
    except:
        print 'Bad link'
        docs.write(url)
        docs.close()
    
    
#***************************************

#Process HTML and store to file****************

    docs1 = open(docnumber , 'r+')
    html = docs1.read()
    soup = BeautifulSoup(html, "html.parser")
    raw = soup.get_text()
    raw = raw.encode('ascii','ignore')
    #print(raw)
    prodocs = open(prodocnumber, 'w+')
    html = docs1.read()
    prodocs.write(raw)
    prodocs.close()
#*********************************************

#Close files, iterate counter forward***
    
    print line
    i = i + 1
#***************************************

   
