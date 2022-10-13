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
load_dotenv()
key = os.environ.get('API_KEY')
def historical(ticker):
   url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey='+key+'&datatype=csv'
   df = pd.read_csv(url)
def close_hist(df):
   plt.hist(df.close, bins=100)
   plt.title("Closing Price Histogram")
   plt.ylabel('Number of per bin')
   plt.xlabel('Price')
   print(plt.show())
def open_hist(df):
   plt.hist(df.open, bins=100)
   plt.title("Opening Price Histogram")
   plt.ylabel('Number of per bin')
   plt.xlabel('Price')
   print(plt.show())
def low_hist(df):
   plt.hist(df.low, bins=100)
   plt.title("Day Low Histogram")
   plt.ylabel('Number of per bin')
   plt.xlabel('Price')
   print(plt.show())
def high_hist(df):
   plt.hist(df.high, bins=100)
   plt.title("Day High Histogram")
   plt.ylabel('Number of per bin')
   plt.xlabel('Price')
   print(plt.show())
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
      try:
         match = soup.find('div', class_="QXDnM").text
         print(match)
      except:
         None
      statsData = getData(stats(ticker))
      financialsData = getData(financials(ticker))
      marketCap(statsData)
      profibility(statsData)
      marketShare(financialsData)
def getPrice(soup):
   try:
      match = soup.find('div', class_='YMlKec fxKbKc').text
      return currencyConversion(match)
   except:
      return 0
def getClimateScore(soup):
   try:
      s = BS(requests.get(soup.find("div", class_="fvysid").find('a')['href']+"?per_page=20&sort_by=project_year&sort_dir=desc").text, 'lxml')
      try:
         return s.find('div', class_='investor-program__score_band_single tooltip-top investor-program__score_band--climate-change').text.replace('\n','')
      except:
         return 'None'
   except:
      return 'None'
def stats():
   return 'https://finance.yahoo.com/quote/{}/key-statistics?={}'
def financials():
   return 'https://finance.yahoo.com/quote/{}/financials?p={}'
def getData(url):
   response = requests.get(url.format(ticker, ticker), headers=headers)
   soup = BS(response.text, 'html.parser')
   pattern = re.compile(r'\s--\sData\s--\s')
   scriptData = soup.find('script', text=pattern).contents[0]
   start = scriptData.find('context')-2
   return json.loads(scriptData[start:-12])
def marketShare(financialsData):
	try:
		return 100 * (financialsData['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly'][0]['revenue']['raw']-financialsData['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly'][0]['earnings']['raw'])/financialsData['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly'][0]['revenue']['raw']  
	except KeyError:
		return 0
def marketCap(statsData):
   try:
      return statsData['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['marketCap']['longFmt']
   except:
      return 0
def profibility(statsData):
	try:
		return statsData['context']['dispatcher']['stores']['QuoteSummaryStore']['financialData']['profitMargins']['raw']
	except KeyError:
		return 0
if __name__ == '__main__':
    main()