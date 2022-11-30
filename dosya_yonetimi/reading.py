# try:
#     file = open("dosya_yonetimi/newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma başarısız")
# finally:
#     print("Dosya kapandı")
#     file.close()


# file = open("dosya_yonetimi/newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="")

#*************** read() fonksiyonu

# content = file.read()
# print("içerik 1")
# print(content)


# content2 = file.read()
# print("içerik 2")
# print(content2)
# print()

# content = file.read(5)
# content = file.read(3)
# content = file.read(5)

# print(content)
# file.close()





# ************ readline() fonksiyonu  satır okur

# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline())
# print(file.readline())
# file.close()


# ************ readlines() fonksiyonu (listedir) 
# her satırı liste elemanı olarak ele alır

# print(file.readlines())

# liste= file.readlines()
# print(liste[1],end="")
# file.close()





#************** okuma fonksiyonları 
# with bir nevi döngüdür döngüden çıktığınız zaman dosya kapanır.
# with open("dosya_yonetimi/newfile.txt","r",encoding="utf-8") as file:

#     content = file.read()
#     print(content)
#     file.seek(0) ## imleci istediği index numarasına getirir
#     print(file.tell()) ## imleç kaçıncı indexte onu öğrenir 
#     content2 = file.read()
#     print(content2)