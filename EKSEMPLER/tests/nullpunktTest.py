from SBmathLib import *

a = 0
b = 5
N = 10000

tol = 1E-15

def f(x):
    return x**2-x-2

def fder(x):
    return newtonskvotient(f, x, tol)

print(NewtonsMetode(a, tol, N, f, fder))
print(halveringsmetoden(a, b, tol, N, f))


