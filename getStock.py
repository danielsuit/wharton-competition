#import os
#from dotenv import load_dotenv
#import numpy as np
#import pandas as pd
#from matplotlib import pyplot as plt
import csv
#stocks = pd.read_csv('stocklist.csv')
#print(stocks.head)
from bs4 import BeautifulSoup as BS
import requests
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
def exchangeConversion(exchange):
   if exchange == 'B3 S.A.':
      exchange = 'BVMF'
   elif exchange == 'BSE LTD':
      exchange = 'BOM'
   elif exchange == 'Hong Kong Exchanges And Clearing Ltd':
      exchange = 'HKG'
   elif exchange == 'London Stock Exchange':
      exchange = 'LON'
   elif exchange == 'Nasdaq':
      exchange = 'NASDAQ'
   elif exchange == "New York Stock Exchange Inc.":
      exchange = 'NYSE'
   elif exchange == 'Shanghai Stock Exchange':
      exchange = 'SHA'
   elif exchange == 'Shenzhen Stock Exchange':
      exchange = "SHE"
   elif exchange == 'Toronto Stock Exchange':
      exchange = "TSE"
   return exchange
def currencyConversion(price):
   if price[0] == '$':
      price = price.replace(',', '')
      price = float(price[1:])
   elif price[0] == '₹':
      price = price.replace(',', '')
      price = float(price[1:])*0.012
   elif price[0:2] == 'R$':
      price = price.replace(',', '')
      price = float(price[2:])*0.19
   elif price[0] == '¥':
      price = price.replace(',', '')
      price = float(price[1:])*0.14
   elif price[0:3] == 'GBX':
      price = price.replace(',','')
      price = float(price[6:])*0.0113
   return round(price, 2)
def getPrice(ticker, exchange):
   exchange = exchangeConversion(exchange)
   url = 'https://www.google.com/finance/quote/{}:{}'
   response = requests.get(url.format(ticker, exchange), headers=headers).text
   soup = BS(response, 'lxml')
   try:
      match = soup.find('div', class_='YMlKec fxKbKc').text
      match = currencyConversion(match)
   except:
      return 0
   return match
class GetStock:
   def __init__(self, number, name, ticker, exchange, industryGroup, industry, subIndustry, no):
      self.number = number;
      self.name = name;
      self.ticker = ticker;
      self.exchange = exchange;
      self.industryGroup = industryGroup;
      self.industry = industry;
      self.subIndustry = subIndustry;
      self.no = no;
   def __str__(self):
      return f"{self.number} | {self.name} | {self.ticker} | {self.exchange} | {self.industryGroup} | {self.industry} | {self.subIndustry} | {self.no}";
stockList = [];
with open("stocklist.csv") as csvfile:
   reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE);
   for row in reader:
      stockList.append(row);
for i in range(len(stockList)):
   x = GetStock(i, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6])
def sortStockList(stocklist):
   for i in range(len(stockList)):
      stocklist[i] = stockList[i][1], stockList[i][0], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]
      #ticker, name, exchange, industryGroup, industry, subIndustry
   return stockList
def insertPrice(stocklist):
   stockList = sortStockList(stocklist)
   for i in range(len(stockList)):
      price = getPrice(stockList[i][0], stocklist[i][2])  
      stockList[i] = [price, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]]
      print(stockList[i])
   stockList.sort()
   print(stockList)
insertPrice(stockList)