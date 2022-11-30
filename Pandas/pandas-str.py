import pandas as pd

data = pd.read_csv("data/nba.csv")
data.dropna(inplace = True)  #  data = data.dropna()   ile aynı görevi görür

# data["player_name"] = data["player_name"].str.upper()
# data["player_name"] = data["player_name"].str.lower()
# data["index"] = data["player_name"].str.find("a")
# data = data[data["player_name"].str.contains("Jordan")] #  =======>>> içerisinde Jordan olan verileri getirir
# data = data["college"].str.replace(' ','-').str.replace('*','')  # stringte değiştirme methodu

data[["FirstName","LastName"]] = data["player_name"].loc[data["player_name"].str.split().str.len()==2].str.split(expand=True) # Player_name kolonunu boşluktan 
# itibaren böldüğümüzde uzunluğu 2 tane veri oluyorsa FirstName ile LastName Kolonu oluşturur ve oraya atar.



print(data.head(10))