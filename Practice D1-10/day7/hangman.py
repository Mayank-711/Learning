import random
import wordlist
import symbol
endgame = False
word = [random.choice(wordlist.word_list)]
print(symbol.logo)
display = []
lives = int("6")
choosen_word = random.choice(word)
for b in choosen_word:
    display += "_"
print(display)
while not endgame:
    guess = input("Guess a letter:").lower()
    for a in range(len(choosen_word)):
        c = choosen_word[a]
        if c == guess:
            display[a] = guess
    if guess not in choosen_word and lives > 0:
        lives -= 1
        print(symbol.stages[lives])
    elif lives==0:
        print("You Lose")
        break
    print(",".join(display))
    if "_" in display:
        endgame = False
    else:
        endgame = True
        print("You won")
