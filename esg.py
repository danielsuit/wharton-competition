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
   try:
      s = BS(requests.get(BS(requests.get('https://www.google.com/finance/quote/{}:{}'.format(ticker, exchangeConversion(exchange)), headers=headers).text, 'lxml').find("div", class_="fvysid").find('a')['href']+"?per_page=20&sort_by=project_year&sort_dir=desc").text, 'lxml')
      try:
         cc = s.find('div', class_='investor-program__score_band--climate-change investor-program__score_band_single tooltip-top').text.replace('\n', '')
      except:
         cc = 'None'
      try:
         forests = s.find('div', class_='investor-program__score_band--forests investor-program__score_band_single tooltip-top').text.replace('\n', '')
      except:
         forests = 'None'
      try:
         water = s.find('div', class_='investor-program__score_band--water investor-program__score_band_single tooltip-top').text.replace('\n', '')
      except:
         water = 'None'
      print([cc, forests, water])
      return [cc, forests, water]
   except:
      print("None")
      return "None"
def sortStockList(stocklist):
   results = []
   for i in range(len(stockList)):
      results.append([stockList[i][1], stockList[i][0], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
   return results
def insertClimateScore(stocklist):
   stockList = sortStockList(stocklist);
   results = [];
   scoreA = [];
   scoreB = [];
   scoreC = [];
   scoreD = [];
   scoreF = [];
   for i in range(len(stockList)):
      climateScore = getClimateScore(stockList[i][0], stocklist[i][2])
      if climateScore[0] == "A" or climateScore[0] == "A-":
         scoreA.append([climateScore, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
      elif climateScore[0] == "B" or climateScore[0] == "B-":
         scoreB.append([climateScore, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
      elif climateScore[0] == "C" or climateScore[0] == "C-":
         scoreC.append([climateScore, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
      elif climateScore[0] == "D" or climateScore[0] == "D-":
         scoreD.append([climateScore, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
      elif climateScore[0] == "F":
         scoreF.append([climateScore, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
      results.append([climateScore, stockList[i][0], stockList[i][1], stockList[i][2], stockList[i][3], stockList[i][4], stockList[i][5], stockList[i][6]])
   print(datetime.datetime.now()-start)
   print("A: "+str(scoreA))
   print("B: "+str(scoreB))
   print("C: "+str(scoreC))
   print("D: "+str(scoreD))
   print("F: "+str(scoreF))
   print(results)
insertClimateScore(stockList)
class ESGRating:
   def __init__(self, score, size):
      self.score = score;
      self.size = size;