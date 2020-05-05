word = 'Escape Room er kult! Python er kult! Teams er kult! Mats og Tom er kule!'
summ = 0

sumList = [ord(c) for c in word]

for i in sumList:
    summ += i

print(summ)

#6294