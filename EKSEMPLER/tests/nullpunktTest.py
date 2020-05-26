
a = 0
b = 5
maxIter = 10000

tol = 1E-10

def f(x):
    return x**2-x-2

c = (a+b)/2

i = 0
while i < maxIter and abs(f(c)) > tol:
    if f(c) == 0:
        a = b = c
    elif f(c)*f(a) < 0 :
        b = c
    else:
        a = c
    i += 1
    c = (a+b)/2

print("Found x=", c, "Iteration: ", i)    