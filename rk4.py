from math import sin
from numpy import arange
from pylab import plot, show


def f(x,t):
	return -x**3 + sin(t)

a = 0.0
b = 10.0

#Euler
N = 1000
h = (b-a)/N

x = 0.0

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
	xpoints.append(x)
	x += h*f(x,t)                  

plot(tpoints, xpoints)

#RK2
N = 20
h = (b-a)/N

x = 0.0

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
	xpoints.append(x)
	k1 = h*f(x,t)                  
	k2 = h*f(x + 0.5*k1,t + 0.5*h) 
	x += k2

plot(tpoints, xpoints)

#4th order runge-kutta
N = 20
h = (b-a)/N

x = 0.0

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
	xpoints.append(x)
	k1 = h*f(x,t)           
	k2 = h*f(x + 0.5*k1,t + 0.5*h)
	k3 = h*f(x + 0.5*k2,t + 0.5*h)
	k4 = h*f(x + k3,t + h)
	x += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0

plot(tpoints, xpoints,'bo')

show()
