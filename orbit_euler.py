from math import sin, pi, sqrt
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel, axes
import matplotlib.pyplot as plt

ty0 = 0.0
ty1 = 10.0
t0 = ty0*3.15569e7
t1 = ty1*3.15569e7
N = 10000
h = (t1-t0)/N

G = 6.673e-11
M = 1.98e30

tpoints = arange(t0,t1,h)
xpoints = []
ypoints = []

r = array([1.49e11, 0.0, 0.0, 29800.0],float)

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
        d = sqrt(r[0]*r[0] + r[1]*r[1])
        ax = -r[0]*G*M/d/d/d
        ay = -r[1]*G*M/d/d/d
        r[0] += h*r[2]
        r[1] += h*r[3]
        r[2] += h*ax
        r[3] += h*ay

plot(xpoints, ypoints)

axes().set_aspect('equal', 'datalim')
xlabel("x")
ylabel("y")
show()

