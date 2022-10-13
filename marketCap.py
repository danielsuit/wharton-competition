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
def marketCap(ticker):
	urlStats = 'https://finance.yahoo.com/quote/{}/key-statistics?={}'
	urlFinancials = 'https://finance.yahoo.com/quote/{}/financials?p={}'
	response = requests.get(urlStats.format(ticker, ticker), headers=headers)
	soup = BS(response.text, 'html.parser')
	pattern = re.compile(r'\s--\sData\s--\s')
	scriptData = soup.find('script', text=pattern).contents[0]
	start = scriptData.find('context')-2
	jsonData = json.loads(scriptData[start:-12])
	try:
		return jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['price']['marketCap']['longFmt']
	except KeyError:
		return 0
print(marketCap("MSFT"))
def marketShare(ticker):
	urlStats = 'https://finance.yahoo.com/quote/{}/key-statistics?={}'
	urlFinancials = 'https://finance.yahoo.com/quote/{}/financials?p={}'
	response = requests.get(urlFinancials.format(ticker, ticker), headers=headers)
	soup = BS(response.text, 'html.parser')
	pattern = re.compile(r'\s--\sData\s--\s')
	scriptData = soup.find('script', text=pattern).contents[0]
	start = scriptData.find('context')-2
	jsonData = json.loads(scriptData[start:-12])
	try:
		return 100 * (jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly'][0]['revenue']['raw']-jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly'][0]['earnings']['raw'])/jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['earnings']['financialsChart']['yearly'][0]['revenue']['raw']  
	except KeyError:
		return 0
print(marketShare("MSFT"))
def profibility(ticker):
	urlStats = 'https://finance.yahoo.com/quote/{}/key-statistics?={}'
	urlFinancials = 'https://finance.yahoo.com/quote/{}/financials?p={}'
	response = requests.get(urlStats.format(ticker, ticker), headers=headers)
	soup = BS(response.text, 'html.parser')
	pattern = re.compile(r'\s--\sData\s--\s')
	scriptData = soup.find('script', text=pattern).contents[0]
	start = scriptData.find('context')-2
	jsonData = json.loads(scriptData[start:-12])
	try:
		return jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['financialData']['profitMargins']['raw']
	except KeyError:
		return 0
print(profibility("MSFT"))

