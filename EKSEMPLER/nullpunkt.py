
# f(startValue) og f(endValue) må ha forskjellig fortegn
startValue = 0
endValue = 5

tol = 1E-10
iterations = 1000

i = 0

# Definerer funksjonen


def f(x):
    return x**2-x-2


# Halveringsmetoden
c = (startValue+endValue)/2  # Finner første halvering

while i < iterations and abs(f(c))>tol:
    if f(c) == 0:
        startValue = endValue = c
    elif f(startValue)*f(c) < 0:
        endValue = c
    else:
        startValue = c
    i +=1
    c = (startValue+endValue)/2

print("Løsningen på likningen er x =", c, "og løkken gikk", i, "ganger")
