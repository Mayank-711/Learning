import random
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
lc= int(input("How many letters would you like in your password?\n"))
sc = int(input(f"How many symbols would you like?\n"))
nc = int(input(f"How many numbers would you like?\n"))
a=random.choices(l,None,k=lc-sc-nc)
b=random.choices(s,None,k=sc)
c=random.choices(n,None,k=nc)
password = []
for letter in a:
    password+=letter
for no in b:
    password+=no
for sy in c:
    password+=sy
random.shuffle(password)
ans="".join(password)
print(f"Your Generated Password is:{ans}")