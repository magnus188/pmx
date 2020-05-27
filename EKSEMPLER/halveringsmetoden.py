from MTmathLib import *

# f(startValue) og f(endValue) må ha forskjellig fortegn
startValue = 0
endValue = 5

tol = 1E-15
N = 1000

i = 0

# Definerer funksjonen


def f(x):
    return x**2-x-2


# Halveringsmetoden
c = (startValue+endValue)/2  # Finner første halvering

print(halveringsmetoden(startValue,endValue,tol,N,f))
