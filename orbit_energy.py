from math import sin, pi, sqrt
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel, axes, xlim, ylim, grid
import matplotlib.pyplot as plt

ty0 = 0.0
ty1 = 10.0
t0 = ty0*3.15569e7
t1 = ty1*3.15569e7
N = 300
h = (t1-t0)/N

G = 6.673e-11
M = 1.98e30
R0 = 1.496e11
E0 = G*M/R0

def f(r,t):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    d = sqrt(x*x + y*y)
    ax = -x*G*M/d/d/d
    ay = -y*G*M/d/d/d
    return array([vx,vy,ax,ay],float)

tpoints = arange(t0,t1,h)
xpoints = []
ypoints = []
rpoints = []
vpoints = []
Epoints = []

r = array([1.496e11, 0.0, 0.0, 29800.0],float)
#r = array([1.496e11, 0.0, 0.0, 20800.0],float)

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
        rad = sqrt(r[0]*r[0] + r[1]*r[1])
        vel = sqrt(r[2]*r[2] + r[3]*r[3])
        E = -G*M/rad + 0.5*vel*vel
	rpoints.append(rad)
	vpoints.append(vel)
	Epoints.append(E)
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1,t+0.5*h)
        k3 = h*f(r + 0.5*k2,t+0.5*h)
        k4 = h*f(r + k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6.0

xau = [x/1.496e11 for x in xpoints]
yau = [y/1.496e11 for y in ypoints]
En = [e/E0 + 0.5for e in Epoints]
tn = [t/3.15e7 for t in tpoints]


plt.subplot(2,1,1)
plot(xau, yau)
xlim(-2.85,2.85)
ylim(-1.1,1.1)
xlabel("x (AU)")
ylabel("y (AU)")
#plot(xpoints, ypoints)

plt.subplot(2,1,2)
plot(tn,En)
xlabel("t (years)")
ylabel("delta E")
#plot(tpoints, Epoints)
#ylim(-4.44e8,-4.42e8)

if 0:
    axes().set_aspect('equal', 'datalim')
#grid(2.0)

show()

