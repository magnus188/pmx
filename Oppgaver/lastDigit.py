
def lastDigit(a,b,c):
    if (a%10==b%10 or a%10==c%10 or b%10 == c%10):
        #Two or more last digits are equal
        return True
    else:
        return False

print(lastDigit(23,19,13))
print(lastDigit(23,19,12))
print(lastDigit(23,19,3))
print(lastDigit(23,19,39))