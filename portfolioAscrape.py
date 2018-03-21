import bs4
from bs4 import BeautifulSoup
import requests

url ="https://rossthorn.github.io"
result = requests.get(url)
c = result.content

soup = BeautifulSoup(c, 'html.parser')

for a in soup.find_all('a', href=True):
    print "A page exists at "+url+'/'+ a['href']
    pageUrl = url+'/'+a['href']
    pageResult = requests.get(pageUrl)
    pagec = pageResult.content

    pageSoup = BeautifulSoup(pagec, 'html.parser')

    projectText = pageSoup.find("h4")
    if projectText is not None:
        pageText = projectText.text
        print pageText
