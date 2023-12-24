from data import data
from art import logo
from art import vs
import random

def game():
    endgame = False
    score = 0
    while endgame == False:
        print(logo)
        one = random.randint(0, len(data)-1)
        two = random.randint(0, len(data)-1)
        A = data[one]
        B = data[two]
        print(f"Compare A:{A["name"]},{A["description"]},{A["country"]}")
        print(vs)
        print(f"Against B:{B["name"]},{B["description"]},{B["country"]}")
        response = input("Guess Who has more followers? A or B:")
        a_count = int(A["follower_count"])
        b_count = int(B["follower_count"])
        if response == "A" and a_count > b_count:
            score += 1
            print(f"You're right,Current score is {score}")
            continue
        elif response == "B" and b_count > a_count:
            score += 1
            print(f"You're right,Current score is {score}")
            continue
        elif response == "A" and a_count < b_count:
            print(f"You're wrong ,You Lose,Your Score was {score}")
            break
        elif response == "B" and a_count > b_count:
            print(f"You're wrong ,You Lose,Your Score was {score}")
            break
    return score
game()