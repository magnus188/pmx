import sympy as sym
sym.init_printing()
x,y,z,f = sym.symbols('x,y,z,f')
a = sym.Eq(x+y-35)
b = sym.Eq(x+z-27)
c = sym.Eq(y+f-50)
d = sym.Eq(y+c-38)

solved = sym.solve([a,b,c,d],(x,y,z,f))

print(solved)

