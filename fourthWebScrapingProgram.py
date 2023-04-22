#Fourth Webscraping program
#Header2 Scraping
from bs4 import BeautifulSoup
with open('index.html', 'r') as html_file:
            content = html_file.read()

            soup = BeautifulSoup(content, 'lxml')
            headerTwoLines = soup.find_all('h2')
            for lines in headerTwoLines:
                        print(lines.text)
                                           
