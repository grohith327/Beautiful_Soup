import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Lionel_Messi').read()
soup = bs.BeautifulSoup(sauce,'lxml')


for url in soup.find_all('a'):
    print(url.get('href'))
    
