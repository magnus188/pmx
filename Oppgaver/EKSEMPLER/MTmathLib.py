
#Derivasjon
def newtonsKvotient(f,x,delta_x):
    fder = (f(x+delta_x)-f(x))/delta_x
    return fder

def newtonsSymmetriske(f,x,delta_x):
    fder = (f(x+delta_x)-f(x-delta_x))/2*delta_x
    return fder

#Integrasjon
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


