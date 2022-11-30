import os
import datetime
# result = dir(os)
# result = os.name  # hangi işletim sistemini kullandığımı gösterir


# os.chdir('C://')   # Dizin değiştirebilir
# os.chdir('..') # bir üst dizine geçer 


# os.mkdir("newdirectory") # bulunduğumuz dizinde klasör oluşturur
# os.makedirs("newdirectory/yeniklasör") # klasörler oluşturur
# os.rename("newdirectory","yeniklasor") #klasör ismi değiştirme
# os.rmdir("newdirectory") # klasörü siler
# os.removedirs("yeniklasör/yeniklasör") # alt dizindeki klasörleri de siler

# result = os.getcwd() # bulunduğumuz dizini öğrenir

# result = os.listdir() # etkin dizindekileri gösterir



#***** Sadece .py uzantılı dosyaları gösterir ******
# for dosya in os.listdir():
#     if dosya. endswith('.py'):
#         print(dosya)



# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihi


# os.system("notepad.exe") # notepad.exe dosyasını çalıştırır.


# path
result = os.path.abspath("_os.py") # dosyanın  konumunu öğrenir.
result = os.path.dirname("C:/Users/Abdullah/Desktop/python_temelleri/_os.py") # tam konumu verilen adresin dizin ismini öğrenir.
result = os.path.dirname(os.path.abspath("_os.py")) # dosyanın tam yolunu bulur ve dizin ismini verir
result = os.path.exists("C:/Users/Abdullah/Desktop/python_temelleri/_os.py") #aradığın konumda dosya var mı 
print(result)
