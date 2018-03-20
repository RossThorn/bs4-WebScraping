# bs4-WebScraping
A simple example of web scraping and crawling with BeautifulSoup4 python package.

Created for UW-Madison Cart Lab Education Series (CLES)

Install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Requests](http://docs.python-requests.org/en/master/) to run these examples!

The scripts scrape [my portfolio](https://rossthorn.github.io/) for all the projects on the page. *portfolioAscrape.py* goes to each project page to extract the text description of each project. 

If you'd rather write the outputs to a file, simply replace all print statements with file writing code:

## Adapting *portfolioscrape.py* to write projects to file

### Open a file at the beginning of the script.
```python
file = open("Projects.txt","w") 
```

### Replace print statement with code that writes it to the open file.
```python
for project in projects:
    file.write(project.text+"\n")
```
### Finally, close the file at the end of the script.
```python
file.close()
```

This code is a must-have for any hardcore Ross Thorn fan that wants to keep up to date on what I'm doing.
