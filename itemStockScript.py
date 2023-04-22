import requests
import time
status = "sold"

r = requests.get("webpage")
if status in r.text:
    soldout = True
while soldout == True:
    r = requests.get("webpage")
    if status in r.text:
        print("sold out")
        time.sleep(60)

print("Item is in stock")
##############################
while True:
    page = requests.get('webpage')
    if status not in page.text:
        break
    print('Item is sold out')
    time.sleep(60)
##############################

from bs4 import BeautifulSoup
import requests

def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("text", {"class": "product-inventory"})
    print(out_of_stock_divs)
    return len(out_of_stock_divs) != 0

def check_inventory():
    url = "https://www.newegg.com/hp-prodesk-400-g5-nettop-computer/p/N82E16883997492?Item=9SIA7ABC996974"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        print("In stock")
    else:
        print("Out of stock")

while True:
    check_inventory()
    time.sleep(60)
################################
    
import requests
from bs4 import BeautifulSoup


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("div", {"class": "product-inventory"})  # <--- change "text" to div
    print(out_of_stock_divs)
    return len(out_of_stock_divs) != 0

def check_inventory():
    url = "https://www.newegg.com/hp-prodesk-400-g5-nettop-computer/p/N82E16883997492?Item=9SIA7ABC996974"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        print("In stock")
    else:
        print("Out of stock")

check_inventory()
    
