import tensorflow as tf
import os
import csv
import datetime 
import tensorflow_hub as hub
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
from dotenv import load_dotenv
from matplotlib import pyplot as plt
from historicalData import *
from exchangeConversion import *
from currencyConversion import *
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
with open("stocklist.csv") as csvfile:
   stockList = [];
   reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE);
   for row in reader:
      stockList.append(row);
class StockList:
   def __init__(self, number, name, ticker, exchange, sector, industryGroup, industry, subIndustry):
      self.number = number;
      self.name = name;
      self.ticker = ticker;
      self.exchange = exchange;
      self.sector = sector;
      self.industryGroup = industryGroup;
      self.industry = industry;
      self.subIndustry = subIndustry;
   def __str__(self):
      return f"{self.number} | {self.name} | {self.ticker} | {self.exchange} | {self.sector} | {self.industryGroup} | {self.industry} | {self.subIndustry}";
def sortByPrice(stockList):
   results = []
   for i in range(len(stockList)):
      results.append([stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
   return results
def sortByESG(stockList):
   results = []
def main():
   start = datetime.datetime.now()
   print(start)
   for i in range(len(stockList)):
      stock = StockList(i, stockList[i][0], stockList[i][1], exchangeConversion(stockList[i][2]), stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6])
      print(stock.number, stock.name)
      url = 'https://www.google.com/finance/quote/{}:{}'.format(stock.ticker, stock.exchange)
      soup = BS((requests.get(url, headers=headers).text), 'lxml')
      print(getPrice(soup))
      print(getClimateScore(soup))
def getPrice(soup):
   try:
      match = soup.find('div', class_='YMlKec fxKbKc').text
      return currencyConversion(match)
   except:
      return 0
def getClimateScore(soup):
   try:
      s = BS(requests.get(soup.find("div", class_="fvysid").find('a')['href']+"?per_page=20&sort_by=project_year&sort_dir=desc"), 'lxml')
      try:
         return s.find('div', class_='investor-program__score_band_single tooltip-top investor-program__score_band--climate-change').text.replace('\n','')
      except:
         return 'None'
   except:
      return "None"
if __name__ == '__main__':
    main()