from math import sin, pi, sqrt
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel, axes, xlim, ylim, grid
import matplotlib.pyplot as plt

ty0 = 0.0
ty1 = 3.0
t0 = ty0*3.15569e7
t1 = ty1*3.15569e7
N = 30000
h = (t1-t0)/N

G = 6.673e-11
M1 = 1.98e30
M2 = 0.1*M1


def f(r,t):
    M2x = r[0]
    M2y = r[1]
    mx = r[2]
    my = r[3]
    M2vx = r[4]
    M2vy = r[5]
    mvx = r[6]
    mvy = r[7]
    M2d = sqrt(M2x*M2x + M2y*M2y)
    M2ax = -M2x*G*M1/M2d/M2d/M2d
    M2ay = -M2y*G*M1/M2d/M2d/M2d
    mx2 = mx - M2x
    my2 = my - M2y
    md = sqrt(mx*mx + my*my)
    md2 = sqrt(mx2*mx2 + my2*my2)
    m_ax = -mx*G*M1/md/md/md -mx2*G*M2/md2/md2/md2 
    m_ay = -my*G*M1/md/md/md -my2*G*M2/md2/md2/md2 
    return array([M2vx,M2vy,mvx,mvy,M2ax,M2ay,m_ax,m_ay],float)

tpoints = arange(t0,t1,h)
M2xpoints = []
M2ypoints = []
mxpoints = []
mypoints = []

r = array([1.49e11, 0.0, (0.5*1.496e11), 0.0,   0.0, 29800.0, 0.0, 1.4*29800.0],float)

for t in tpoints:
	M2xpoints.append(r[0])
	M2ypoints.append(r[1])
	mxpoints.append(r[2])
	mypoints.append(r[3])
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1,t+0.5*h)
        k3 = h*f(r + 0.5*k2,t+0.5*h)
        k4 = h*f(r + k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6.0

M2xn = [x/1.496e11 for x in M2xpoints]
M2yn = [y/1.496e11 for y in M2ypoints]
mxn = [x/1.496e11 for x in mxpoints]
myn = [y/1.496e11 for y in mypoints]

plot(M2xn, M2yn)
plot(mxn, myn)

axes().set_aspect('equal', 'datalim')
xlim(-1.5,1.5)
ylim(-1.5,1.5)
xlabel("x")
ylabel("y")
show()

