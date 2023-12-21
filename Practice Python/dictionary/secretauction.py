from ui import logo

print(logo)
print("Welcome to auction")
auction = {}
stop = False
while stop == False:
    name = input("What is your name?:")
    bid = int(input("What is your bid?:"))
    auction[name] = bid
    a = input("Any other Bidder?Yes or No:")
    if a == "Yes":
        stop = False
    else:
        stop = True
def highest(abc):
    hbid=0
    winner=""
    for b in abc:
        price = abc[b]
        if price>hbid:
            hbid=price
            winner=b
    print(f"The winner is {winner} of {hbid}")
highest(auction)