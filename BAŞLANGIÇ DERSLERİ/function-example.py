# def message(mesaj,k):
#     while k>0:
#         print(mesaj)
#         k=k-1

# mesaj = input(' Mesajınızı giriniz :')
# dongu = int(input('Mesajın kaç kere döneceğini giriniz :'))
# message(mesaj,dongu)


# #----------------------------------------



# def asalBulma(num1,num2):
#     while num1 <= num2:
        
#         sayac = True
#         for i in range(2,num1):
#             if (num1 % i == 0):
            
#                 sayac = False
#                 break

#         if sayac == True:
#             print(f'{num1} is prime number.')
        
#         num1 = num1 + 1


# num1 = int(input('1. Sayıyı Giriniz :'))
# num2 = int(input('2. Sayıyı Giriniz :'))
# asalBulma(num1, num2)


# #----------------------------------------------



num = int(input('Enter the Number : '))

def divisor(n):
    divisorlist = []
    for k in range(1, n+1):
        if n % k == 0:
            divisorlist.append(k)
    return divisorlist
        
result = divisor(num)
print(result)