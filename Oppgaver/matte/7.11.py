from MTmathLib import *
import pylab as pl

def f(x):
    return (100*x**2+1000)/(1.07*x**3+45)

x = pl.arange(0,101,0.1)
print(x)
fder = newtonsKvotient(f,x,10**-8)

print(max(fder))
print("År med høyest stigning:", int(pl.where(fder == pl.amax(fder))[0]+1))

pl.plot(f(x), color="red", label="f(x)")
pl.plot(fder, color="b", label = "f'(x)")
pl.axvline(color="k")
pl.axhline(color="k")
pl.grid()
pl.legend()

pl.show()


