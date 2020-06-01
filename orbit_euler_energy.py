from math import sin, pi, sqrt
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel, axes, subplot
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
rpoints = []
vpoints = []
Epoints = []

r = array([1.49e11, 0.0, 0.0, 29800.0],float)

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
        rad = sqrt(r[0]*r[0] + r[1]*r[1])
        vel = sqrt(r[2]*r[2] + r[3]*r[3])
        E = -G*M/rad + 0.5*vel*vel
	rpoints.append(rad)
	vpoints.append(vel)
	Epoints.append(E)
        d = sqrt(r[0]*r[0] + r[1]*r[1])
        ax = -r[0]*G*M/d/d/d
        ay = -r[1]*G*M/d/d/d
        r[0] += h*r[2]
        r[1] += h*r[3]
        r[2] += h*ax
        r[3] += h*ay

subplot(2,1,1)
plot(xpoints, ypoints)
xlabel("x")
ylabel("y")

subplot(2,1,2)
plot(tpoints,Epoints)
xlabel("t")
ylabel("E")

#axes().set_aspect('equal', 'datalim')
show()

