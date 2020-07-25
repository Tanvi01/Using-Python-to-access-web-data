#!/usr/bin/env python
# coding: utf-8

# In[29]:


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count =int(input('Enter count - '))
pos = int(input('Enter pos- '))

for i in range(count):
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url=tags[pos-1].get('href',None)
    print(url)


# #### 
