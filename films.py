import csv
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
from fpdf import FPDF


def fetchUrl(url):
  opener = request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0')]
  request.install_opener(opener)
  htmlSring = request.urlopen(url).read()
  return htmlSring.decode()


filmsHtml = fetchUrl('https://www.filmweb.pl/ranking/wantToSee/next30daysPoland')
filmsSoup = BeautifulSoup(filmsHtml, features="html.parser")
AllFilmsInfo = filmsSoup.find_all('div', {'class': 'item place'})

filmsData = []


for filmInfo in AllFilmsInfo:
    filmData = []
    filmTitle = filmInfo.find('a', {'class': 'film__link'}).text
    premiereDate = filmInfo.find('div', {'class': 'film__premiere'}).text
    wtsCounter = filmInfo.find('span', {'class': 'film__wts-count'}).text
    productionYear = filmInfo.find('span', {'class': 'film__production-year'}).text[1:5]
    filmData.append(filmTitle)
    filmData.append(premiereDate)
    filmData.append(wtsCounter)
    filmData.append(productionYear)
    filmsData.append(filmData)



labels=['Title', 'Premiere Date', 'Year', 'People who want to see']
df1=pd.DataFrame.from_records(filmsData)

with open('films.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(labels)
    for n in filmsData:
        csvwriter.writerow(n)



