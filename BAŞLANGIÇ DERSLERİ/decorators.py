import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        print("1 saniye bekleyeceksiniz")
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print(func.__name__ +" Fonksiyonu "+ str(finish-start)+" saniye sürdü.")
    return inner


@calculate_time 
def usalma(a,b):
    print(math.pow(a,b))
    
    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num)) 

@calculate_time
def toplama(a,b):
    print(a+b)
    
    
usalma(2,3)
toplama(29,2)
faktoriyel(5)