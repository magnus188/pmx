import pylab as pl

n = 10
a = 0
b = 44

numbers = []

for i in range(n):
    m = a+i*(b-a)/(n-1)
    numbers.append(m)

print(numbers)
print(pl.linspace(a,b,n))