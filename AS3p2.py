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
List = []
#i = iter(List)

for line in open('test2.html','r'):
    a = line
    b = a.index(':')
    a = a[:b]
    print a
    if a not in List:
        List.append(a)
        i = i + 1
        print i
print i
    
