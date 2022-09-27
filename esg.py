from bs4 import BeautifulSoup as BS
import requests, csv, datetime
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
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
stockList = [];
with open("stocklist.csv") as csvfile:
   reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE);
   for row in reader:
      stockList.append(row);
def getClimateScore(ticker, exchange):
   exchange = exchangeConversion(exchange)
   url = 'https://www.google.com/finance/quote/{}:{}'
   response = requests.get(url.format(ticker, exchange), headers=headers).text
   soup = BS(response, 'lxml')
   try:
      match = soup.find_all("div", class_="P6K39c")
      for i in match:
         try:
            if soup.find_next("div", class_="P6K39c") == 'A':
               print('A')
               return 'A'
         except:
            continue
      print(match)
      return match
   except:
      return 0
def sortStockList(stocklist):
   results = []
   for i in range(len(stockList)):
      results.append([stockList[i][1], stockList[i][0], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
   return results
def insertClimateScore(stocklist):
   stockList = sortStockList(stocklist)
   results = []
   for i in range(len(stockList)):
      climateScore = getClimateScore(stockList[i][0], stocklist[i][2])
      print(climateScore)  
      results.append([climateScore, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
   print(datetime.datetime.now()-start)
   print(results)
insertClimateScore(stockList)
class ESGRating:
   def __init__(self, score, size):
      self.score = score;
      self.size = size;