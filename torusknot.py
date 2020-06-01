from math import sin,cos,pi
from numpy import array,arange,linspace
from pylab import plot, show, xlabel, ylabel

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

p = 5.0
q = 2.0

N = 1000

phip = linspace(0,2*pi,N)
xpoints = []
ypoints = []
zpoints = []

for phi in phip:
    r = 0.5*(2.0 + sin(q*phi))
    xpoints.append(r*cos(p*phi))
    ypoints.append(r*sin(q*phi))
    zpoints.append(-sin(p*phi))

#plot(tpoints, ypoints)
ax.plot(xpoints, ypoints, zpoints)
xlabel("x")
ylabel("y")
show()

