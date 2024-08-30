# Password Generator

import random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a',
        'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol=['!','@','#','$','%','&','*','(',')']
number=['0','1','2','3','4','5','6','7','8','9']
print("Welcome to the password generator !!")
print()
a=int(input(("How many letter you want in a password:")))
b=int(input(("How many symbol you want in a password:")))
c=int(input(("How many number you want in a password:")))

list=[]
for i in range(1,a+1):
    list+=random.choice(letter)
for i in range(1,b+1):
    list+=random.choice(symbol)
for i in range(1,c+1):
    list+=random.choice(number)
random.shuffle(list)
password=''
for char in list:
    password+=char
print('Your generated password is:',password)