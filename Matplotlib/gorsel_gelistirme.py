import numpy as np
import matplotlib.pyplot as plt


numpyDizisi1 = np.linspace(0,10,20)
numpyDizisi2 = numpyDizisi1**2

yeniFigur = plt.figure()  # dpi=150
yeniEksen = yeniFigur.add_axes([0.1,0.1,0.9,0.9])
yeniEksen.plot(numpyDizisi1,numpyDizisi2,label = "numpyDizisi **2")
yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 3,label="numpyDizsi**3")
yeniEksen.legend(loc=2)   # çizgilerin labellarımı isimlerini gösterir      #loc lokasyo belirtir tablonunnerede olması gerektiğini gösterir
plt.show()
yeniFigur.savefig("benimfigur.png",dpi =200)