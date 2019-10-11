import re
from random_word import RandomWords


print("Welcome to hangman")

word = RandomWords().get_random_word()
hiddenWord = ""
lives = 8

for i in range(len(word)):
    hiddenWord += "_"

def convert(s): 
    new = ""   
    for x in s: 
        new += x  
    return new

while "_" in hiddenWord:
    userInput = str(input("Guess a letter: "))
    if (userInput == word):
        break
    elif (len(userInput) != 1):
        print("Choose only one letter!")
        pass
    elif ("_" not in hiddenWord):
        print("You won with", lives, "left")
        break
    else:
        if (userInput in word and userInput not in hiddenWord):
            for match in re.finditer(userInput, word):
                s = list(hiddenWord)
                s[match.start()] = userInput
                hiddenWord = convert(s)
                print("\n")
                print(" ".join(hiddenWord))
        elif(userInput in word):
            print("\nYou have already guessed this letter")
            pass
        else:
            if(lives == 0):
                print("You loose")
                break
            else:
                lives -= 1
                print("\nWrong guess\nLives left:", lives)


print("You won with", lives, "lives left")
         

