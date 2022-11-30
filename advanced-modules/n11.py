import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
list = soup.find("div",{"id":"view"}).find_all("li")
for pro in list:
    name = pro.find("a").find("h3",{"class":"productName"}).text 
    link = pro.div.a.get("href")
    old_price = pro.find("div",{"class":"priceContainer"}).find("span").find("del").text
    new_price = pro.find("div",{"class":"priceContainer"}).find("span").findNextSibling().find("ins").text
    print(f"{name} LİNK = {link} \nESKİ FİYATI={old_price} YENİ FİYATI={new_price}\n")
