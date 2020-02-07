import pylab as pl
import math

n = 10 # steps
a = 0.0 # start
b = 10.0 # stop
step = (b-a)/(n-1) # calculate step
y0 = 0 # initialbetingelse

x = pl.zeros(n) # nullmatrise x
y = pl.zeros(n) # nullmatrise y

# yder funksjon
def yder(y,x):
    return (3*x**2+4*x-y)/x

# sett initialbetingelse
y[0] = y0
x[1]=1
# eulers metode
for i in range(1,n-1):
    print(yder(y[i], x[i]))
    y[i+1] = y[i] + yder(y[i], x[i])*step
    x[i+1] = x[i] + step

# plot
pl.plot(x,y)
pl.grid()
#pl.show()

