# for every number from 1 to 100
# if dividable by 3 -> Fizz

for i in range(1,100):
    if (i%3 == 0 and i%5 != 0):
        print("FIZZ")
    elif (i%5==0 and i%3 != 0):
        print("BUZZ")
    elif (i%3 == 0 and i%5 == 0):
        print("FIZZBUZZ")
    else:
        print(i)