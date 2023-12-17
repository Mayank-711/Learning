print("Welcome to treasure hunt your mission is to find the treasure")
A=input("Where would you like to go left or right:")
if A == "left":
    B = input("Would you like to wait for boat or swim:")
    if B == "wait":
        C=input("Choose a color between red,yellow,green:")
        if C =="yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game over")
else:
    print("Game Over")