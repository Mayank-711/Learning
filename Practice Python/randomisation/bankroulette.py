import random
names = input("Enter the name of The persons use comma to seperate:")
list1= names.split(",")
b = len(list1)
a = random.randint(0,b)
print(list1[a]+" Has to pay the bill")