import csv, requests
from bs4 import BeautifulSoup as BS
def getUrl(ticker, exchange):
    with open('stocklist.csv','r') as csvinput:
        with open('C:/test/output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)
            row.append('Berry')
            all.append(row)
            for i in reader:
                s = BS(requests.get(BS(requests.get('https://www.google.com/finance/quote/{}:{}'.format(ticker, exchangeConversion(exchange)), headers=headers).text, 'lxml').find("div", class_="fvysid").find('a')['href']+"?per_page=20&sort_by=project_year&sort_dir=desc").text, 'lxml')
                requests.get

            for row in reader:
                row.append(row[0])
                all.append(row)
            writer.writerows(all)