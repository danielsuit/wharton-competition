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
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
import datetime
start = datetime.datetime.now()
print(start)
def exchangeConversion(exchange):
   if exchange == 'B3 S.A.':
      return 'BVMF'
   elif exchange == 'BSE LTD':
      return 'BOM'
   elif exchange == 'Hong Kong Exchanges And Clearing Ltd':
      return 'HKG'
   elif exchange == 'London Stock Exchange':
      return 'LON'
   elif exchange == 'Nasdaq':
      return 'NASDAQ'
   elif exchange == 'New York Stock Exchange Inc.':
      return 'NYSE'
   elif exchange == 'Shanghai Stock Exchange':
      return 'SHA'
   elif exchange == 'Shenzhen Stock Exchange':
      return 'SHE'
   elif exchange == 'Toronto Stock Exchange':
      return 'TSE'
   return exchange
def currencyConversion(price):
   if price[0] == '$':
      price = price.replace(',', '')
      return round(float(price[1:]),2)
   elif price[0] == '₹':
      price = price.replace(',', '')
      return round(float(price[1:])*0.012,2)
   elif price[0:2] == 'R$':
      price = price.replace(',', '')
      return round(float(price[2:])*0.19,2)
   elif price[0] == '¥':
      price = price.replace(',', '')
      return round(float(price[1:])*0.14,2)
   elif price[0:3] == 'GBX':
      price = price.replace(',','')
      return round(float(price[6:])*0.0113,2)
   return float(price)
def getPrice(ticker, exchange):
   exchange = exchangeConversion(exchange)
   url = 'https://www.google.com/finance/quote/{}:{}'
   response = requests.get(url.format(ticker, exchange), headers=headers).text
   soup = BS(response, 'lxml')
   try:
      match = soup.find('div', class_='YMlKec fxKbKc').text
      return currencyConversion(match)
   except:
      return 0
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
def sortStockList(stocklist):
   results = []
   for i in range(len(stockList)):
      results.append([stockList[i][1], stockList[i][0], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
   return results
def insertPrice(stocklist):
   stockList = sortStockList(stocklist)
   for i in range(len(stockList)):
      price = getPrice(stockList[i][0], stocklist[i][2])  
      stockList[i] = [price, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]]
   stockList.sort()
   print(datetime.datetime.now()-start)
   print(stockList)
insertPrice(stockList)