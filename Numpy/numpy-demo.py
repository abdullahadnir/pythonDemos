import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
result = np.array([10,15,30,45,60])
# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
result = np.arange(5,15)
# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
result = np.arange(50,100,5)
# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
result = np.zeros(10)
# 5- 10 elamanlı birlerden oluşan bir dizi oluşturunuz.
result = np.ones(10)
# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
result = np.linspace(0,100,5)
# 7- (10-30) arasında rastgele 5 sayı üretiniz.
result = np.random.randint(10,30,5)
# 8- [-1 ile 1] arasında 10 adet sayı üretin.
result = np.random.randn(10)
# 9- (3x5) boyurlarında (10-50) arasında rastgele bir matris oluşturun.
result1 = np.random.randint(10,50,5)
result2 = np.random.randint(10,50,10)
result = np.hstack((result1,result2)).reshape(3,5)
print(result)
# 10- üretilen matrisin satır ve sütun toplamlarını hesaplayınız.
print(result.sum(axis=1))
print(result.sum(axis=0))
# 11- üretilen matrisin en büyük, en küçük ve ortalaması nedir 
print(result.max())
print(result.min())
# 12- üretilen matrisin en büyük değerin indeksi nedir
print(result.argmax())
# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçin.
dogruluk = result[0:3,0:0] <= 20
print(result[dogruluk])
    
print(dogruluk)
# 14- üretilen dizinin elemanlarını tersten yazdırın.
print(result1[::-1])
print(result2[::-1])
# 15- üretilen matrisin ilk satırını seçiniz.
print(result[0:1])
# 16- üretilen matrisin 2.satır 3. sütundaki elemanı hangisidir.
print(result[1][2])
# 17- üretilen matrisin tüm satırlardaki ilk elemanı seçiniz
print(result[::][0])
# 18- üretilen matrisin her bir elemanın karesini alınız.
print(result*result)
# 19- üretilen matris elemanlarının hangisi pozitif çift sayıdır? Aralığı (-50,+50)


matris = np.random.randint(-50,50,15).reshape(3,5)
print(matris)
ciftler = matris[matris % 2 == 0]
pozitif = ciftler[ciftler>0]
print(pozitif)



