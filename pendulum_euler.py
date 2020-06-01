from math import sin, pi
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel
import matplotlib.pyplot as plt

t0 = 0.0
t1 = 3.0
N = 3000000
h = (t1-t0)/N

g = 9.81
l = 0.1

tpoints = arange(t0,t1,h)
thpoints = []
opoints = []

theta0 = 179.0*(pi/180)
omega0 = 0.0*(pi/180)
r = array([theta0,omega0],float)

for t in tpoints:
	thpoints.append(r[0])
	opoints.append(r[1])
        fomega = -(g/l)*sin(r[0])
        r[0] += h*r[1]
        r[1] += h*fomega

thdpoints = [180/pi*x for x in thpoints]

plot(tpoints, thdpoints)

xlabel("t")
ylabel("theta")
show()

