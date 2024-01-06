import random
from ui import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
endgame = False
while endgame == False:
    print(logo)
    ans = input("Do you want to play blackjack? Yes or No:")
    if ans == "Yes":
        user = random.choices(cards, k=2)
        computer = random.choices(cards, k=2)
    else:
        print("End")

    print(f"Your Card are:{user}")
    print(f"Computer First Card is :{computer[0]}")

    newcard = input("Do you want another card?Yes or No:")
    if newcard == "Yes":
        new = random.choices(cards, k=1)
        user.extend(new)

    print(f"New Cards{user}")
    card2user = sum(user)
    card2computer = sum(computer)

    if 11 in user:
        if card2user > 21:
            card2user -= 10
    elif 11 in computer:
        if card2computer > 21:
            card2user -= 10

    while card2computer < 16:
        compcard = random.choices(cards, k=1)
        computer.extend(compcard)
        card2computer = sum(computer)
    def winloss():
        print(f"Cards of Computer:{computer}")
        print(f"Cards of User:{user}")
        if card2computer == 21:
            if card2user == 21:
               print("Blackjack for Computer you lose")
            elif card2user < 21:
               print("Blackjack for Computer you lose")
        elif card2user == 21:
            if card2computer == 21:
               print("Draw")
            elif card2computer < 21:
               print("You win")
        elif card2user > 21:
            print("You Bust")
        elif card2computer > 21 and card2user > 21:
            print("Both Bust")
        elif card2computer > card2user:
           print("Computer Wins You Lose")
        else:
           print("You win")
    winloss()
    ans = input("Do you want to play another round of blackjack? Yes or No:")
    if ans == "Yes":
         endgame=False
    else:
        endgame=True
