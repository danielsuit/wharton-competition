from bs4 import BeautifulSoup as BS
from dotenv import load_dotenv
from matplotlib import pyplot as plt
import requests, csv, pandas as pd, lxml, os, numpy as np
import re, json
from io import StringIO
from lxml import html
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
def getPrice(ticker):
	urlStats = 'https://finance.yahoo.com/quote/{}/key-statistics?={}'
	urlFinancials = 'https://finance.yahoo.com/quote/{}/financials?p={}'
	response = requests.get(urlStats.format(ticker, ticker), headers=headers)
	soup = BS(response.text, 'html.parser')
	pattern = re.compile(r'\s--\sData\s--\s')
	scriptData = soup.find('script', text=pattern).contents[0]
	start = scriptData.find('context')-2
	jsonData = json.loads(scriptData[start:-12])
	try:
		regPrice = jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['regularMarketPrice']
	except KeyError:
		return 0
	price = 0
	for i in regPrice:
		try:
			price = regPrice['fmt']
		except TypeError:
			continue
		except KeyError:
			continue
	return price