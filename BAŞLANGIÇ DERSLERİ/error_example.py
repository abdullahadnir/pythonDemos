# liste = ["1","2","5a","10b","abc","10","50"]
# """ 1 : LİSTE ELEMANLARI İÇİNDEKİ SAYISSAL DEĞERLERİ BULUR """
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue








    
# """Kullanıcı 'q' değeri girmedikçe her
# inputun sayı olup olmadığını kontrol eder."""

# while True:
#     sayi = input("Sayı Giriniz :")
#     if  sayi == "q":
#         print("Uygulamadan Çıkış Yapılıyor !!!!!")
#         break
#     try:
#         number = int(sayi)
#         print("Girdiğiniz Değer Sayıdır.")
#     except ValueError:
#         print("Girdiğiniz İnput değeri sayı değildir")









# """Girilen Parola İçinde Türkçe Hatası Verir"""

# def check_password(psw):
#     import re
#     if  re.search("[ıöşçüğİÖĞŞÇÜ]",psw):
#         raise Exception("Paraloda Türkçe Karakter Olmamalıdır ")
#     else:
#         print("Geçerli Parola Girdiniz ")

# password = input("Parola Giriniz : ")
# check_password(password)










# """Faktöriyel fonksiyonu oluşturup her türlü hatayı verir"""
# def factorial(number):
#     result = 1
#     while number > 1:
#         result = number*result
#         number -= 1
#     return result
# while True:
#     number = input("Faktöriyelini almak istediğiniz sayıyı giriniz :")
#     try:
#         number = int(number)
#         if number < 0:
#             raise Exception("Negative değer giremezsiniz")
#     except Exception as ex:
#         print(ex)
#         break
#     else:
#         print(factorial(number))