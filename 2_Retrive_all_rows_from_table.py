import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')


#for url in soup.find_all('table'):
#    print(url.get('href'))

tables = soup.find_all('tr')

for row in tables:
    td = row.find_all('td')
    l = []
    for i in td:
        l.append(i.text)
    print(l)
    
    
