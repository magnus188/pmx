import pylab as pl

# Derivasjon
def newtonsKvotient(f,x,delta_x):
    fder = (f(x+delta_x)-f(x))/delta_x
    return fder

def newtonsSymmetriske(f,x,delta_x):
    fder = (f(x+delta_x)-f(x-delta_x))/2*delta_x
    return fder

# Integrasjon
def rektangelMetoden(f,a,b,n):
    total = 0.0
    h = (b-a)/n
    for k in range(0,n):
        total += f(a+(k*h))
    areal = h*total
    return areal

def trapesMetoden(f,a,b,n):
    h = (b-a)/n
    total = (f(a)+f(b))/2.0
    for k in range(1,n):
        total += f(a+k*h)
    return h*total

def simpsonsMetoden(f,a,b,n):
    h = (b-a)/n
    total = f(a) + f(b)
    for k in range(1,n,2):
        total += 4*f(a+k*h)
    for k in range(2,n-1,2):
        total += 2*f(a+k*h)
    return total*h/3


# DIFFERENSIALLIKNINGER


def eulersMetode(yder, y0, a, b, N):
    y = pl.zeros(N)
    x = pl.zeros(N)
    h = (b - a)/(N - 1)
    y[0] = y0
    x[0] = a
    for i in range(N - 1):
        y[i+1] = y[i] + h * yder(x[i], y[i])
        x[i+1] = x[i] + h
    return y, x


# NULLPUNKTER (LIKNINGSLØSER)

def newtonsMetode(a, tol, N, f, fder):
    #Definerer intervallet
    #    a = Startverdien
    #    tol = Toleransen
    #    N = Antall iterasjoner
    #    f = funksjonen
    #    fder = den deriverte av funksjonen

    i = 1  # Tellevariabel
    c = 1  # Nullpunktsvariabel

    #Newtons metode
    while i <= N and abs(f(c)) >= tol:
        c = a - f(a)/fder(a)
        a = c
        i += 1

    return c


def halveringsmetoden(a, b, tol, n, f):

    #a = Startverdi
    #b = Sluttverdi
    #tol = Toleranse
    #n = Antall ganger løkka kan kjøre
    i = 1  # Tellevariabel

    #Halveringsmetoden
    c = (a + b)/2  # Finner første halveringspunkt
    while i < n and abs(f(c)) > tol:
        if f(c) == 0:
            a = b = c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
        i += 1
        c = (a + b)/2

    return c


