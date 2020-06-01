from math import pi
from numpy import arange,sin,cos,zeros,linspace
from pylab import plot, show, ylim

N = 1000
x = linspace(0.0,pi,N+1)
y = zeros(len(x),float)

i = 0
for i in range(N):
    y[i] = sin(x[i])

xr = x[1:N] # this is the central 99 points of x

h = x[1] - x[0]

dydx = zeros(len(xr),float)

for i in range(1,N-1,1):
    dydx[i] = (y[i+1] - y[i])/1.0/h

plot(xr, (dydx - cos(xr)),"ko")
ylim(-0.005,0.005)
show()


