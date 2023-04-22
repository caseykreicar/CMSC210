#Sixth Webscraping program
#My real website scraping
from bs4 import BeautifulSoup
import requests
htmlText = requests.get('https://www.bestbuy.com/site/pny-xlr8-gaming-single-fan-nvidia-geforce-gtx-1660-super-overclocked-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6407309.p?skuId=6407309').text
print(htmlText)
soup = BeautifulSoup(htmlText, 'lxml')
