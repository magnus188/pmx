import pylab as pl

N = 1000
a = 0.0
b = 1.0
h = (b-a)/(N-1)
y0 = 0

def yder(y,x):
    return y

x = pl.zeros(N)
y = pl.zeros(N)

y[0] = y0

# Eulers metode
for i in range(N-1):
    y[i+1] = y[i] + yder(y[i], x[i]*h)
    x[i+1] = x[i] + h

print(y[0:N:100])

pl.plot(x,y)
pl.grid(True)
pl.show()
