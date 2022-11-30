import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns= ["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"]  => loc[":","column"]
result = df.loc["A"]
result = (type(df.loc["A"]))
result = df.iloc[2]           # index leri değiştirsek bile index numarasını kullan

result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]  # Column 1 ile Column 2 yi al
result = df.loc[:,:"Column2"]           #Başlangıçtan Column2 ye kadar al
result = df.loc[:,"Column2":"Column3"]  # Column2 den Column 3 e kadar al
result = df.loc["A":"B",:"Column2"]     # A dan B ye kadar Column 2 leri al
result = df.loc[:"B",:"Column2"]        #B ye ladar olan Column2  leri al

result = df.loc["A","Column2"]          # A indexine sahip satırın Column2 sini al
result = df.iloc[1,2]                # 1(B satırı) indexine sahip satırın 2(Column3) indexine sahip sütunun al
result = df.loc[["A","B"],["Column1","Column2"]]   # A ve B satırının Column1 ile Column2  sini getir

# print(result)


df["Column4"] = pd.Series(randn(3),["A","B","C"])   # Column 4 ü dataframe e ekler
df["Column5"] = df["Column1"] + df["Column3"]       # C1 ile c3 ün toplamını Column 5 olarak ekle


result = df.drop("Column5",axis=1)          #DataFrame de Değişiklik yapmaz sadece resulta Column 5 değerini sildirir
df.drop("Column5",axis=1, inplace= True) # DataFrame den de Column5 i siler


print(result)
print(df)




