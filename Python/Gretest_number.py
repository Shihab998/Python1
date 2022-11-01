a=int(input("Enter 1st your number: "))
b=int(input("Enter 2nd your number: "))
c=int(input("Enter 3rd your number: "))
d=int(input("Enter 4th your number: "))

if(a>d):
    f1=a
else:
    f1=d
if(b>c):
    f2=b
else:
    f2=c
if(f1>f2):
    print(str(f1)+" is Gretest number")
if(f2>f1):
    print(str(f2)+" is Gretest number")   


