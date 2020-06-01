from math import sin, pi
from random import random
from numpy import linspace, zeros, array, asarray
from pylab import plot, show

#filter size
di = 4 #full boxcar filter width is 2*this + 1

# make array for independent variable t
t0 = 0.0
t1 = 5.0
N = 300
ts = linspace(t0, t1, N)

# parameters for functional form
P = 2.0
om = 2.0*pi/P
a = 0.5

# plot with two arrays
vs = zeros(N,float)
for i in range(N):
    vs[i] = sin(om*ts[i]) + a*random()
#plot(ts,vs)

# now boxcar filter vs
svs = zeros(N,float)
w = 1.0/(2.0*float(di) + 1.0) #normalized weighting

for i in range(di, N-di, 1):
    for j in range(-di, di+1, 1):
        svs[i] += w*vs[i+j]
# handle ends of range - in this case, just set equal to unfiltered data
for i in range(0,di,1):
    svs[i] = vs[i]
for i in range(N-di,N,1):
    svs[i] = vs[i]

plot(ts,svs, linewidth=3) 
show()



