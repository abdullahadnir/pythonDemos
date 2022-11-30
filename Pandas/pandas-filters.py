import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5",])

result = df
result = df.columns      # kolon isimlerini alırız
result = df.head()       # İlk 5 tane satırı(kaydı) alır
result = df.head(10)     # İlk 10 tane satırı alır
result = df.tail()       # Son 5 tane satırı alır
result = df.tail(10)     # Son 10 tane satırı alır
result = df["Column1"].head()   # İlk 5 kaydın Columns1 lerini alır
result = df.Column1.head()
result = df[["Column1","Column2"]].head(10)  # İlk 10 kaydının Kolon1 ve Kolon2 sini alır
result = df[["Column1","Column2"]].tail(10)  # Son 10 kaydının Kolon1 ve Kolon2 sini alır
result = df[5:15][["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].tail()

result = df > 50    # Hücrelerden 50 de büyük olanlara True değeri atar
result = df[df>50]  # hücrelerdel, 50 den büyük olanları alır
result = df[df % 2 == 0]  #hücrelerdeki çiftleri gösterir

result = df[df["Column1"] > 50]     # kolon1 de 50 den büyük olanların kayıtlarını getirir
result = df[df["Column1"] > 50][["Column1","Column2"]] # Kolon 1 in 50 den büyük ollanlarının kolon 1 ve kolon 2 lerini getir
result = df[(df["Column1"] > 50) & (df["Column1"] < 70)]  # Column 1 i 50 den büyük 70 ten küçük olan satırları getirir.
result = df[(df["Column1"] > 50) & (df["Column2"] < 70)][["Column1","Column2"]]
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1","Column2"]]  # | veya işareti
result = df.query("Column1 >= 50 & Column1 % 2 == 0")   # Diğer kullanımı
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]    
result = df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]]


print(result)