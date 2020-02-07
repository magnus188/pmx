import pylab as pl
import math

# difflikning
# y' +y^3= sin(x)
# y(0) = 0


n = 10000 # steps
a = 0.0 # start
b = 10.0 # stop
step = (b-a)/(n-1) # calculate step
y0 = 0 # initialbetingelse

x = pl.zeros(n) # nullmatrise x
y = pl.zeros(n) # nullmatrise y

# yder funksjon
def yder(y,x):
    return math.sin(x)-y**3

# sett initialbetingelse
y[0] = y0

# eulers metode
for i in range(n-1):
    y[i+1] = y[i] + yder(y[i], x[i])*step
    x[i+1] = x[i] + step

# plot
pl.plot(x,y)
pl.grid()
pl.show()

