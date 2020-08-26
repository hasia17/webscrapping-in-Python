from urllib import request
from bs4 import BeautifulSoup


def fetchUrl(url):
  opener = request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0')]
  request.install_opener(opener)
  htmlSring = request.urlopen(url).read()
  return htmlSring.decode()


moviesHtml = fetchUrl('https://www.filmweb.pl/serials/premiere')
moviesSoup = BeautifulSoup(moviesHtml, features="html.parser")
AllMovieInfo = moviesSoup.find_all('div', {'class': 'premieresList__dayRange'})

for movieInfo in AllMovieInfo:
    movieTitle = movieInfo.find('h2', {'class': 'filmPreview__title'}).text
    print(movieTitle)
    premiereDate = movieInfo.find('h2', {'class': 'premieresList__dayHeader'})
    premiereDate2 = premiereDate.find('time', {'class': 'formatDate'}).text

    print(movieTitle)
    print(premiereDate)
    print(premiereDate2)

