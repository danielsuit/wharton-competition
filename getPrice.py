headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
from currencyConversion import *; from exchangeConversion import *; import requests; from bs4 import BeautifulSoup as BS
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