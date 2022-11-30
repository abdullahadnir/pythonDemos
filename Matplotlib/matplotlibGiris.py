import numpy as np
import matplotlib.pyplot as plt

yasListesi = [10,20,30,30,30,40,50,60,70,75]
kiloListesi = [20,60,80,85,86,87,70,90,95,90]

numpyYasListesi = np.array(yasListesi)
numpyKiloListesi = np.array(kiloListesi)

plt.plot(numpyYasListesi,numpyKiloListesi,"blue")  #plt.plot(x ekseni, y ekseni,"renk")
plt.title("Kilonun Yaşa Göre Değişim Grafiği")
plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.show()  #grafik çıktısını verir

numpyDizisi1 = np.linspace(0,10,20)
numpyDizisi2 = numpyDizisi1**3
plt.plot(numpyDizisi1,numpyDizisi2,"r*-")   #kesik çizgili gösterir.("b--"")
plt.show()

plt.subplot(1,2,1) 
plt.plot(numpyDizisi1,numpyDizisi2,"r*-")   #1 sıra olacak 2 kolon olacak şu an 1. grafiği çizeceğiz
plt.subplot(1,2,2)
plt.plot(numpyDizisi2,numpyDizisi1,"b--")   #1 sıra olacak 2 kolon olacak şu an 2. grafiği çizeceğiz
plt.show()


# KENDİN ÖZELLEŞTİRİLMİŞ GRAFİĞİNİ OLUŞTURMA
benimFigure = plt.figure()
figureAxes = benimFigure.add_axes([0.1,0.1,0.7,0.7])
figureAxes.plot(numpyDizisi1,numpyDizisi2,"g")
figureAxes.set_xlabel("X ekseni Veri ismi ")
figureAxes.set_ylabel("Y ekseni  Veri ismi")
figureAxes.set_title("Grafik Başlığı")
plt.show()

# İç İçe Grafikler
figure2 = plt.figure()
eksen1 = figure2.add_axes([0.1,0.1,0.7,0.7])
eksen2 = figure2.add_axes([0.1,0.4,0.3,0.3])

eksen1.plot(numpyDizisi1,numpyDizisi2,"g")
eksen1.set_xlabel("X ekseni Veri ismi ")
eksen1.set_ylabel("Y ekseni  Veri ismi")
eksen1.set_title("Ana Grafik Başlık")

eksen2.plot(numpyDizisi1,numpyDizisi2,"b")
eksen2.set_xlabel("X ekseni Veri ismi ")
eksen2.set_ylabel("Y ekseni  Veri ismi")
eksen2.set_title("Küçük Grafik Başlık")
plt.show()

