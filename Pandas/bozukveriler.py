import pandas as pd
import numpy as np
# personeller ={
#     'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
#     'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','Bilgi İşlem'],
#     'Yaş':[30,25,45,50,23,34,42],
#     'Semt':['Kadıköy','Tuzla','Maltepe','Tuzla','Kadıköy','Tuzla','Maltepe'],
#     'Maaş':[5000,3000,4000,3500,2750,6500,4500]
# }

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])
df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,31,np.nan,50,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop(["column1","column2"],axis=1) # Kolonları siler
result = df.drop(["a","b","h"],axis=0)         # Satırları siler

result = df.isnull()    #gelen sonuçlar içerisinden NuN olanlara TRUE değeri yazdırır
result = df.notnull()    #gelen sonuçlar içerisinden NuN olanlara FALSE değeri yazdırır
result = df.isnull().sum()
result = df["column1"].isnull().sum()

result = df[df["column1"].isnull()]
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]
result = df[df["column1"].notnull()]

result = df.dropna()  #axis= 0 ==> satıra NULL değeri içeren satırları siler
result = df.dropna(axis=1)  #axis= 1 ==> sütuna NULL değeri içeren sütunları siler
result = df.dropna(how= "any")   # herhangi birtane NULL değeri varsa satırı siler
# result = df.dropna(how= "all")   # tüm değerler NULL  ise satırı siler
result = df.dropna(subset= ["column1","column2"],how="any") # column1 ve column2 ye bakarak siler
result = df.dropna(thresh= 2) # en az 2 tane normal veri varsa silme
result = df.dropna(thresh= 3) # en az 3 tane normal veri varsa silme
result = df.dropna(thresh= 4) # en az 4 tane normal veri varsa silme

result = df.fillna(value= "no input") # değeri NaN olanlara no input yaazar
result = df.fillna(value= 1)    # değeri NaN olanlara 1 değerini atar




result = df.sum()
result = df.sum().sum()
result = df.size
result= df.isnull().sum()
result= df.isnull().sum().sum()

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value = ortalama(df))






print(ortalama(df))
print(result)

