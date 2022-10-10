from bs4 import BeautifulSoup as BS
import requests, csv, datetime, threading
start = datetime.datetime.now()
print(start)
stockList = [];
with open("stocklist.csv") as csvfile:
   reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE);
   for row in reader:
      stockList.append(row);
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
   try:
      for i in scoreA:
         print(str(i)+"Company name: "+str(scoreA[1])+": Climate Score: "+str(scoreA[0][0])+"Ticker: "+str(scoreA[2]))
      for i in scoreB:
         print(str(i)+"Company name: "+str(scoreB[1])+": Climate Score: "+str(scoreB[0][0])+"Ticker: "+str(scoreB[2]))
      for i in scoreC:
         print(str(i)+"Company name: "+str(scoreC[1])+": Climate Score: "+str(scoreC[0][0])+"Ticker: "+str(scoreC[2]))
      for i in scoreD:
         print(str(i)+"Company name: "+str(scoreD[1])+": Climate Score: "+str(scoreD[0][0])+"Ticker: "+str(scoreD[2]))
      for i in scoreF:
         print(str(i)+"Company name: "+str(scoreF[1])+": Climate Score: "+str(scoreF[0][0])+"Ticker: "+str(scoreF[2]))
   except:
      None
insertClimateScore(stockList)
class ESGRating:
   def __init__(self, score, size):
      self.score = score;
      self.size = size;