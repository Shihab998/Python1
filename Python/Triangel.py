'''
n=int(input('Emter your number: '))

for i in range(n):    #Row
    for j in range(i+1): #Coloum
        print('*',end=' ')
    print()   '''

"""""
n=int(input('Emter your number: '))

for i in range(n):
    for j in range(i,n):
       print('*',end='')
    print()    
"""""
n=int(input('Emter your number: '))

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('* ',end='')  
    print()      