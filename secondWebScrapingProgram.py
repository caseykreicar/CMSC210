#Second Webscraping program
from bs4 import BeautifulSoup
with open('index.html', 'r') as html_file:
            content = html_file.read()

            soup = BeautifulSoup(content, 'lxml')
            print(soup.prettify())
