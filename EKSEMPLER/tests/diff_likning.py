
import pylab as pl


N = 10000
y0 = 0
h = 10E-4

x = pl.zeros(N)
y = pl.zeros(N)

def yder(x,y):
    return x+y**2

y[0] = 0

# Eulers metode
for i in range(N-1):
    y[i+1] = y[i] + yder(y[i], x[i]*h)
    x[i+1] = x[i] + h

pl.plot(x, y)
pl.grid(True)
pl.show()
