import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=None)

count = 1

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text #siteden isim bilgisini çeker
    year = tr.find("td",{"class":"titleColumn"}).find("span").text #siteden yıl bilgisini çeker
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text #imdb puanı 
    
    print(f"{count}- film adı :{title.ljust(80)} yapım yılı :{year} değerlendirme :{rating}")
    count+=1
    