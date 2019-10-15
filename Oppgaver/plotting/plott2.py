import pylab as pl

t = pl.linspace(0,2*pl.pi,1000)

x = 16*pl.sin(t)**3
y = 13*pl.cos(t)-5*pl.cos(2*t)-2*pl.cos(3*t)-pl.cos(4*t)

pl.plot(x,y, color="red")
pl.fill(x,y, color="red")
pl.show()