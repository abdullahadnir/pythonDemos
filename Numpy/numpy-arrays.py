import numpy as np

result = np.array([1,3,5,7,9])
result = np.arange(1,10)
result = np.arange(10,100,3)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0,100,5)
result = np.linspace(0,5,5)
result = np.random.randint(0,10)
result = np.random.randint(20)
result = np.random.randint(1,10,3)
result = np.random.rand(5)
result = np.random.randn(5)

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()
result = rnd_numbers.min()
result = rnd_numbers.mean()     # sayıların ortalaması
result = rnd_numbers.argmax()   # max sayının indexi 
result = rnd_numbers.argmin()   # min sayının indexi
print(result)

# np_array = result = np.arange(50)
# np_multi = np_array.reshape(5,10)
# print(np_multi)
# print(np_multi.sum(axis=1))   # satırların toplamı
# print(np_multi.sum(axis=0))   # sütunların toplamı
