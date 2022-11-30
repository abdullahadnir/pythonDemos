import re
from unittest import result

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#************** RE MODULE***********
# result = re.findall("Python",str) #içerik arar ve liste oluşturur
# result = len(result)


# result = re.split(" ",str) # Bölmelere ayırırız


# result = re.sub(" ","-",str) # değiştirme


# result = re.search("Python",str)  # aramak istediğin şeyi nerden başlayıp bittiğini söyler

# result = result.span() #aradığınız yerin nerede olduğunu söyler
# result = result.start()
# result = result.end()
# result = result.group() #bulduğu ifadeyi getirir 
# result = result.string() # aradığın yeri gösterir



# ********************* REGULAR EXPRESSİON *******************

# result = re.findall("[abc]",str) # a,b,c

# result = re.findall("[a-e]",str) # a,b,c,d,e
# result = re.findall("[1-5]",str) # 1-2-3-4-5
# result = re.findall("[^abc]",str) # abc dışındaki karakterler
# result = re.findall("[^0-9]",str) # rakam olmayan karakterler


# result = re.findall("...",str) # 3 basamaklı olanları arar
# result = re.findall("Pyt..n",str) 

# result = re.findall("^a",str) # a ile başlayanları arar
# result = re.findall("a$",str) # a ile bitenleri arar

# result = re.findall("m*an",str) # bir karakterin sıfır yada daha fazla sayıda olmasını kontrol eder.
 
# result = re.findall("a|b",str) # a ya da b olması 
 
# \ - Özel karakterleri aramamızı sağlar. => \$a dolar işaretini arkasına a harfini arar
 



print(result)