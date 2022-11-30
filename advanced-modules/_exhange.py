import requests
import json

# data = requests.get("https://api.exchangeratesapi.io/v1/symbols?access_key=OzD1juQLCFmD4ZI4aMVMbUjZkkhkvy4q")
# result = json.loads(data.text)
api_url = "https://api.fer.ee/latest?base="


bozulan_doviz = input("Bozulan döviz türü : ")
alinan_doviz = input("Alınan döviz türü : ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz :" ))
result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)
print(f"1 {bozulan_doviz} = {result['rates'][alinan_doviz]} {alinan_doviz}")
print("{0} {1} = {2} {3} ".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz],alinan_doviz))
