import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10
result = numbers1 - numbers2
result = numbers1 - 10
result = numbers1 * numbers2
result = numbers1 * 10
result = numbers1 / 10

result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

mnubers1 = numbers1.reshape(2,3)
mnubers2 = numbers2.reshape(2,3)

# print(mnubers1)
# print(mnubers2)

result = np.vstack((mnubers1,mnubers2)) # matrisleri dikey olarak birleştirir
print(result)
result = np.hstack((mnubers1,mnubers2)) # matrisleri yatay olarak birleştirir
result = numbers1 >= 50
result = numbers1 % 2 == 0
print(numbers1[result])
print(result)
