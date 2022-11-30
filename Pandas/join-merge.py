import pandas as pd

# customers ={
#     'CustomerId':[1,2,3,4],
#     'FirstName':["Ahmet","Ali","Hasan","Canan"],
#     'LastName':["Yılmaz","Korkmaz","Çelik","Toprak"]
#  }

# orders ={
#     "OrderId":[10,11,12,13],
#     "CustomerId":[1,2,5,7],
#     "OrderDate":['2010-07-04','2010-08-04','2010-07-07','2012-07-04',]
# }

# df_customer = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_order = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

# print(df_customer)
# print(df_order)

# result = pd.merge(df_customer,df_order,how="inner")     # dfcustomer dforder tablosunu inner olarak birleştirir 
# result = pd.merge(df_customer,df_order,how="left")     # dfcustomer ların hepsini getir dforder ların ortak olanlarını al    sol tarafı alır
# result = pd.merge(df_customer,df_order,how="right")     # dforder ların hepsini getir dfcustomer ların ortak olanlarını al     sağ tarafı alır
# result = pd.merge(df_customer,df_order,how="outer")     # Bütün Kayıtlar Bize Getirlilir ortak olsun ya da olmasın hepsini alır

customersA ={
    'CustomerId':[1,2,3,4],
    'FirstName':["Ahmet","Ali","Hasan","Canan"],
    'LastName':["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB ={
    'CustomerId':[4,5,6,7],
    'FirstName':["Yağmur","Çınar","Cengiz","Can"],
    'LastName':["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])   # satıra göre birleştirir tabloyu alt alta ekler
result = pd.concat([df_customersA,df_customersB],axis = 1)  # kolona göre birleştirir tabloyu yanına ekler
print(result)