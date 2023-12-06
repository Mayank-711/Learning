print("Welcome")
size = input("Size of Pizza S , M, L:")
peproni = input("Peproni ? Y or N:")
cheese = input("Extra cheese? Yor N")
bill = 0
if size == "S":
    bill+=15
if size == "M":
    bill+=20
if size == "L":
    bill+=25
if peproni =="Y":
    bill+=2
if cheese=="Y":
    bill+=3

print(f"Your Total Bill is{bill}")