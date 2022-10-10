import os
from dotenv import load_dotenv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
load_dotenv()
key = os.environ.get('API_KEY')
def getData(ticker):
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