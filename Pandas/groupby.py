import pandas as pd
import numpy as np

personeller ={
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','Bilgi İşlem'],
    'Yaş':[30,25,45,50,23,34,42],
    'Semt':['Kadıköy','Tuzla','Maltepe','Tuzla','Kadıköy','Tuzla','Maltepe'],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
}
df = pd.DataFrame(personeller)
result = df

result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)


# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)


result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Muhasebe")

result = df.groupby("Departman").sum()  # toplamları
result = df.groupby("Departman").mean() # ortalama
result = df.groupby("Departman")["Maaş"].mean()  #  Departmana göre  sadece Maaş ortalamarı alınır
result = df.groupby("Semt")["Yaş"].mean()       # Semte göre sadece yaşların ortalamasını alır
result = df.groupby("Semt")["Çalışan"].count()  # Semtlere göre çalışan sayısı
result = df.groupby("Departman")["Yaş"].max()   #Yaşa göre alınan en büyük yaş
result = df.groupby("Departman")["Maaş"].min()  # Maaşa göre alınan en az ücret min
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min])   # numpyp kütüphanesi ile birden çok veriye işlem yaptırır agg()
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]







print(result)