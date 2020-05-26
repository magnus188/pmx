import pylab as pl

a = 0
b = 3

amount = 100000

def f(x):
    2*x**3 + x**2 -x + 1


def trapesMetodenMin(f, a, b, n):
    h = (b-a)/n
    tot = (f(a)+f(b))/2.0
    for i in range(n-1):
        tot += f(a+i*h)
    return h*tot


def trapesMetoden(f, a, b, n):
    h = (b-a)/n
    total = (f(a)+f(b))/2.0
    for k in range(1, n):
        total += f(a+k*h)
    return h*total


print(trapesMetodenMin(f,a,b,amount))
print(trapesMetoden(f,a,b,amount))
