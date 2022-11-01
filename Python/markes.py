a=int(input("Enter your math markes: "))
b=int(input("Enter your Bangla markes: "))
c=int(input("Enter your English markes: "))

if(a<33 or b<33 or c<33):
    print("Fail because you less than 30 mark")
elif(a+b+c)/3<40:
    print("fail because you less avg than 40%")
else:
    print("pass")    
