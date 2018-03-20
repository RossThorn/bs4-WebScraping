import bs4
from bs4 import BeautifulSoup

import requests

result = requests.get("https://rossthorn.github.io")
c = result.content

soup = BeautifulSoup(c, 'html.parser')
projects = soup.findAll("div", "overlay-text")

for project in projects:
    print project.text
