import tensorflow as tf
import os
from dotenv import load_dotenv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#stocks = pd.read_csv('stocklist.csv')
#print(stocks.head)
import csv
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
   print(x)

def sortStockList(stocklist):
   for i in range(len(stockList)):
      stocklist[i] = stockList[i][1], stockList[i][0], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]
      #ticker, name, exchange, industryGroup, industry, subIndustry
   print(stocklist)
sortStockList(stockList)