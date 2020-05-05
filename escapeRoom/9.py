word = 'I steg 3 så beregnet du verdiene av strenger slik at Ullern VGS ble til 898. Et annet ord som Passord blir til 732. Her skal vi utvide oppgaven litt. Hvert ord i denne oppgaveteksten har et lykketall. Funksjonen for lykketall er(summen av ASCII verdiene til ordet) % 100 Lykketallet for ordet "oppgave" blir derfor 54. Så for å komme til neste post på programmet så må du nok løse denne oppgaven og finne nummeret til hvert ord. Jeg mente selvfølgelig lykketall. Når det er sagt så er mine lykketall 32, 52, 54 og 77, så alle ord som ikke har disse lykketallene må du fjerne fra oppgaveteksten. Lag et pythonscript som beregner lykketallene til alle ordene i denne oppgaveteksten og print kun de ordene som har mine lykketall. Det er kult å gå på skolen vår ikke sant? Bare for syns skyld. Jeg er ikke interessert i ord som er kortere enn 4 tegn. Disse er det ikke nødvendig å beregne lykketall for. Ok?'

wordList = [n for n in word.split(' ') if len(n) >= 4]

test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lykketall = [32, 52, 54, 77]

print(wordList)

for word in wordList:
    if (sum([ord(c) for c in word])%100 in lykketall):
        print(word)

#0379