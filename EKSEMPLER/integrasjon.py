from MTmathLib import *

startValue = 0
endValue = 5
iterations = 10000  # Amount of Rectangles/Trapes ...

# Define function


def f(x):
    return 2*x**2+x-5


print("Rektangel Metoden: ", rektangelMetoden(
    f, startValue, endValue, iterations))
print("Trapes Metoden: ", trapesMetoden(
    f, startValue, endValue, iterations))
print("Simpsons Metoden: ", simpsonsMetoden(
    f, startValue, endValue, iterations))
