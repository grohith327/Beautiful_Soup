import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('URL').read()
soup = bs.BeautifulSoup(sauce,'lxml')

img = soup.find_all('a',{'class':'image'})
img_list = []

for i in img:
    img_list.append(i.img['src'])
       
for i in range(len(img_list)):
    img_list[i] = 'http:' + img_list[i]

for i in img_list:
    print(urllib.request.urlretrieve(i))
