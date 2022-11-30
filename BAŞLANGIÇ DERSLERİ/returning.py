# ************** İç İçe Fonksiyonlar ********************* 
# def usalma(number):

#     def inner(power):
#         return number ** power
#     return inner

# two = usalma(2)
# print(two(5))  #  2^5 = 32

# three = usalma(3)
# print(three(4))   # 3^4 = 81







# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'admin':
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner
# user1 = yetki_sorgula("Product Edit")
# print(user1("admin"))





# def islem(islem_adi):
#     def toplam(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
    
#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim *= i
#         return carpim
    
#     if islem_adi == "toplama":
#         return toplam
#     else:
#         return carpma
    
# toplama = islem("toplama")
# print(toplama(1,3,5,7,9,45,3))

# carpma = islem("carpma")
# print(carpma(3,4,5))







#  ************* fonksiyonlara parametre gönderme *************
# def toplama(a,b):
#     return a+b
# def cikarma(a,b):
#     return a-b
# def carpma(a,b):
#     return a*b
# def bolme(a,b):
#     return a/b

# def islem(f1,f2,f3,f4,islem_adi):
#     if islem_adi == "toplama":
#         print(f1(10,2))
#     elif islem_adi == "cikarma":
#         print(f2(10,2))
#     elif islem_adi == "carpma":
#         print(f3(10,2))
#     elif islem_adi == "bolme":
#         print(f4(10,2))  
#     else:
#         print("Geçersiz İşlem .....")
    
# islem(toplama,cikarma,carpma,bolme,"İşlem Adı")
# islem(toplama,cikarma,carpma,bolme,"toplama")
# islem(toplama,cikarma,carpma,bolme,"cikarma")
# islem(toplama,cikarma,carpma,bolme,"carpma")
# islem(toplama,cikarma,carpma,bolme,"bolme")