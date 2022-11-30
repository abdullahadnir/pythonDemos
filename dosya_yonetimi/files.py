# Dosya açmak için open() fonksiyonu kullanılır.
#   ==> open(dosya_adi,dosya_erişme_modu)
#       Dosya_erişme_modu ==> dosyayı hangi amaçla açtığımızı belirtir.


#   “w” Write yazma modu. 
#           ** Dosyayı konumda oluşturur.
#           ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("dosya_yonetimi/newfile.txt","w",encoding="utf-8")
# file.write("Abdullah Adanır")
# file.close()



#   “a” append ekleme modu. Dosya konumda yoksa oluşturlur.

file = open("dosya_yonetimi/newfile2.txt","a",encoding="utf-8")
file.write(" Abdullah Adanır(2)\n")
file.close()


#   “x” create oluşturma. dosya varsa hata verir.

# file = open("dosya_yonetimi/newfile2.txt","x",encoding="utf-8")
 
 
 
 

#   “r” read okuma , varsayılan. Dosya konumda yoksa hata verir.
