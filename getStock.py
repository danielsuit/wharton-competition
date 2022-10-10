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
import datetime


def insertPrice(stocklist):
   stockList = sortStockList(stocklist)
   for i in range(len(stockList)):
      price = getPrice(stockList[i][0], stocklist[i][2])  
      stockList[i] = [price, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]]
   stockList.sort()
   print(datetime.datetime.now()-start)
   print(stockList)
insertPrice(stockList)