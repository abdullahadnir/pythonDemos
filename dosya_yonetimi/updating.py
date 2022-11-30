# with open("dosya_yonetimi/newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     print(file.read())
# with open("dosya_yonetimi/newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())





#      ********** Sayfa Sonunda Güncelleme **********
    
# with open("dosya_yonetimi/newfile.txt","a+",encoding="utf-8") as file:
#     file.write("\nsas ")
# with open("dosya_yonetimi/newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())



#     ********** Sayfa Başında Güncelleme  **********

# with open("dosya_yonetimi/newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Ramazan Adanır\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)
    
# with open("dosya_yonetimi/newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())





#     ************* Sayfa Ortasında Güncelleme   *************
    
# with open("dosya_yonetimi/newfile.txt","r+",encoding="utf-8") as file:
#    list = file.readlines()
#    list.insert(1,"Yılmaz Aygün\n")
#    file.seek(0)
#    file.writelines(list)
       

   
# with open("dosya_yonetimi/newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())