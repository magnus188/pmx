from matplotlib import pylab as pl
import math

t = pl.linspace(0,48,49)
y0 = 4.73
a=0.65
y = y0*math.e**-(a*t)

pl.plot(t,y, label="Graph 1", linestyle="dashdot", color="red")


pl.title("Fysssaaaaa")
pl.legend()
pl.grid()
pl.show()