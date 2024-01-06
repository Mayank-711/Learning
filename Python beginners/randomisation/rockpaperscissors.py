import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
  _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
list1 = [rock,paper,scissors]
a = random.randint(0,2)
choose =int(input("Choose 0 for rock,1 for paper,2 for scissors: "))
if choose == 0:
    print("You chose rock\n"+rock)
    print("Computer chose\n"+list1[a])
    if a == 0:
        print("rock")
        print("Its a Draw")
    elif a ==1:
        print("paper")
        print("You Lose")
    else:
        print("scissors")
        print("You win")
elif choose== 1:
    print("You chose paper\n"+paper)
    print("Computer chose\n" + list1[a])
    if a == 0:
        print("rock")
        print("You win")
    elif a == 1:
        print("paper")
        print("Its A draw")
    else:
        print("scissors")
        print("You lose")
elif choose==2:
    print("You chose scissors\n"+scissors)
    print("Computer chose\n" + list1[a])
    if a == 0:
        print("rock")
        print("You Lose")
    elif a == 1:
        print("paper")
        print("You Win")
    else:
        print("scissors")
        print("Its A Draw")