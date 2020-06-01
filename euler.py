from math import sin
from numpy import arange
from pylab import plot, show


def f(x,t):
	return -x**3 + sin(t)

a = 0.0
b = 10.0
N = 10
h = (b-a)/N

x = 0.0

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
	xpoints.append(x)
	x += h*f(x,t)

plot(tpoints, xpoints)

N = 100
h = (b-a)/N

x = 0.0

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
	xpoints.append(x)
	x += h*f(x,t)

plot(tpoints, xpoints)
N = 1000
h = (b-a)/N

x = 0.0

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
	xpoints.append(x)
	x += h*f(x,t)

plot(tpoints, xpoints)
show()

