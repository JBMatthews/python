# Playground

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    count = count + 1
    allhttp = tag.get('href', None)
    for x in allhttp:
        x = allhttp.get('.html')
        print(x)


# DATA
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
