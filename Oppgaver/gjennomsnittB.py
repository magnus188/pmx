
numbers = []
running = True

while running:
    while True:
        try:
            userNumber = int(input('Skriv inn ditt tall mellom 1 og 100: '))
        except ValueError:
            print('Skriv inn et tall!')
            continue
        if (1 <= userNumber <= 100):
            #Valid input
            break
        elif (userNumber == -1):
            running = False
            break
        else:
            #Invalid input
            print("Invalid number. Must be between 1 and 100")
    if running:
        numbers.append(userNumber)
        print('Gjennomsnitt', sum(numbers[-10:])/len(numbers[-10:]))