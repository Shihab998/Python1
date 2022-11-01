text=input("Enter your text ")
spam=False
if('make a lot of money'in text):
    spam=True
elif('bravo'in text):
    spam=True
elif('subscribe'in text):
    spam=True
else:
    spam=False
if(spam):
    print('This text is spam') 
else:
    print('This text is not spam')               