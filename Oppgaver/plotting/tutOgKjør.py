import pylab as pl
from sympy.solvers import solve
from sympy import Symbol

x = pl.linspace(0,20,21)

tut = 1.5*x+20
kjor = 2*x+15


pl.plot(x,tut,label="Tut")
pl.plot(x,kjor,label="Kjør")

intersect = solve(kjor - tut, Symbol('x'))
print(intersect)

#pl.axvline(intersect, color="green")

pl.title("Priser tut vs kjør")
pl.xlabel('Minutter')
pl.ylabel('Pris pr. minutt')
pl.legend()
pl.show()
