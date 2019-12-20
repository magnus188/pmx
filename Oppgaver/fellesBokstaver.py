name1 = str(input('Skriv inn navn 1: '))
name2 = str(input('Skriv inn navn 2: '))

similarCharacters = []

for i in name1.lower():
    if i in name2.lower() and i not in similarCharacters:
        similarCharacters.append(i)

print('Like boksatver', similarCharacters)


