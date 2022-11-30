import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0,10,20)
numpyDizisi2 = numpyDizisi1**2

(benimFigur, benimEksen) = plt.subplots()
benimEksen.plot(numpyDizisi1,numpyDizisi2,"#3A95A8",alpha=0.3)  #alpha = 0-1 arası saydamlık 
benimEksen.plot(numpyDizisi2,numpyDizisi1,"#C96F23")
plt.show()


(yeniFigur, yeniEksen) = plt.subplots()
yeniEksen.plot(numpyDizisi1,numpyDizisi1+2 ,color="blue",linewidth = 5.0)   # linewidth = kalınlık
yeniEksen.plot(numpyDizisi1,numpyDizisi1+3 ,color="green")
yeniEksen.plot(numpyDizisi1,numpyDizisi1+4 ,color ="red",linestyle="-.")
yeniEksen.plot(numpyDizisi1,numpyDizisi1+5 ,color ="red",linestyle=":")
yeniEksen.plot(numpyDizisi1,numpyDizisi1+6 ,color ="red",linestyle="--")

yeniEksen.plot(numpyDizisi1,numpyDizisi1+7 ,color ="black",linestyle="--",marker="o",markersize = 8,markerfacecolor="red") #marker verilerin olduğu yerleri işaretler
plt.show()


#FARKLI GRAFİK ÇEŞİTLERİ 
#SCATTER

plt.scatter(numpyDizisi1,numpyDizisi2)
plt.show()

#Histogram

yeniDizi = np.random.randint(0,100,50)
plt.hist(yeniDizi)
plt.show()

#boxplot

plt.boxplot(yeniDizi)
plt.show()