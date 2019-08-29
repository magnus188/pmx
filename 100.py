import random

print("Skriv inn et tall mellom 1 og 10")

goldenNumbers = [12,23,34,45,56,67,78,89]
sum = 0

def checkResult(i, player):
    global sum
    if (sum + i == 100):
        #Winner, stop game
        print(player, "won")
        sum = 100
    else:
        sum = sum + i
        computerPlay()

def computerPlay():
    if (sum == 0):
        return 1  
    elif (sum > 0 and sum < 90):
        for i in range(len(goldenNumbers)):
            if (sum < goldenNumbers[i]):
                return goldenNumbers[i] - sum
    else:
        return 100 - sum

while sum != 100:
    print("Sum is", sum)
    # Check if between 1 and 10
    while True:
        userInput = int(input("Type your number: "))
        if (0 < userInput <= 10):
            #Valid input
            break
        else:
            print("Invalid number. Must be between 1 and 10")
    checkResult(userInput, "You")
    print("Sum is", sum)
    print("Computer says", computerPlay())
    checkResult(computerPlay(), "Computer")
    