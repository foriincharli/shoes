# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:18:34 2019

@author: Charli
"""

# https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/

# import libraries
from bs4 import BeautifulSoup
import urllib.request as urlr

# specify the url
quote_page = "https://www.windsorsmith.com.au/tennessee-black-croc-ankle-cowboy-boots"
# "https://www.windsorsmith.com.au/ravee-blk-leathe-9362wsw-blk-leathe" use this to find the sale element/test concept 

page = urlr.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

# get product name
name_box = soup.find('span', attrs = {'itemprop':'name'})
name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)

# get product price
price_box = soup.find('span', attrs = {'class':'price'})
price = price_box.text
print(price)

# if on sale
sale_box = soup.find('span', attrs = {'data-price-type':'finalPrice'})
sale = sale_box.text
print(sale)

# make a csv that will contain the above data
import csv
from datetime import datetime

with open('boots.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, price, sale, datetime.now()])
