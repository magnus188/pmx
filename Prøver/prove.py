import random

# list of vocals
vocals = ['a','e','i','o','u','y','z','æ','ø','å']

#convert list to string
def convert(s): 
    new = ""   
    for x in s:
        new += x  
    return str.capitalize(new)

# function to create poem, returns nil but prints output
def createPoem(word:str, author:str, iterations:int):
    print('\''+ word + '\' by', author)
    permutations = set()
    wordList = list(str.lower(word))
    # loop while permutation set is less than number of permutations
    while len(permutations) < iterations:
        unique = True
        random.shuffle(wordList)

        for i in range(len(wordList)):
            # if current letter and previous is both vocals
            if (wordList[i] in vocals and wordList[i-1] in vocals):
                unique = False
        if (unique):
            print(convert(wordList))
            permutations.add(convert(wordList))

createPoem('kulturuke', 'Magnus Trandokken', 20)