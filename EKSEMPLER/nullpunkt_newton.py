from MTmathLib import *

a = 3           # Startpunkt
c = 0           # Nullpunktsvariabel
tol = 10E-8     # Toleranse
N = 10000       # Antall iterasjoner
i = 0           

# Funksjonen
def f(x):
    return x**5 - 5*x**3 -3
                                                      
# Derivert funksjon
def fder(x):
    return 5*x**4 - 15*x**2

# Newtons Metode
print(newtonsMetode(a, tol, N, f, fder))