def squares(m,n):
    small, big = min(m,n), max(m, n)

    amount = 0
    for i in range(small):
        i = i+1
        amount += (big-i+1)*(small-i+1)

    return amount

inputX = int(input("Length of side 1: "))
inputY = int(input("Length of side 2: "))

print(squares(inputX,inputY))


""" print(squares(1,4))
print(squares(4,4))
print(squares(8,4))
print(squares(14,4))
print(squares(4,24)) """
    