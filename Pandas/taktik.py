# A = [1,2,3,4,5]

# if type(A) == ():
#     print("islem gecersiz")
# else:
#     print(list(map(lambda x: x/1, A)))


# A = [[1,2],[3,4],[5,6]]
# print(list(map(lambda x: x[0]*3, A)))

# liste = ["a",20,10,30,"b"]
# print(list(filter(lambda x: type(x) == int, liste)))

# a = [1,2,3]
# print(list(map(lambda x: x*2, a)))


# from functools import reduce
# result = reduce(lambda a,b: a/b, [8,4,2])
# print(result)

# import numpy as np
# a = np.array([1,1,1])
# b = np.array([2])

# print(a+b)


from functools import reduce
a = [1,2,3,4]
result = reduce(lambda a,b: a*b, a)
print(result)

# def yap(x,y,z):
#     try:
#         print(x/y*z)
#     except ZeroDivisionError:
#         print("gecersiz islem")

# yap(1,2,0)
