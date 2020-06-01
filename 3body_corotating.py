from math import cos, sin, pi, sqrt, atan2
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel, axes, xlim, ylim, grid, subplot
import matplotlib.pyplot as plt

AU = 1.496e11
VCAU = 29800.0
MSUN = 1.98e30
G = 6.673e-11
yr = 3.15569e7

ty0 = 0.0
ty1 = 3.0
t0 = ty0*yr
t1 = ty1*yr
N = 30000
h = (t1-t0)/N

M1 = 1.0*MSUN
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
rmxpoints = []
rmypoints = []

if 0:
    mx0 = 0.7*AU
    my0 = 0.0*AU
    mvx0 = 0.0*VCAU 
    mvy0 = 1.0*VCAU

if 0:
    mx0 = 0.5*AU
    my0 = 0.0*AU
    mvx0 = 0.0*VCAU 
    mvy0 = 1.4*VCAU

if 1:
    mx0 = 0.9*AU
    my0 = 0.0*AU
    mvx0 = 0.0*VCAU 
    mvy0 = -0.1*VCAU

r = array([1.49e11, 0.0, mx0, my0,   0.0, 29800.0, mvx0, mvy0],float)

for t in tpoints:
	M2xpoints.append(r[0])
	M2ypoints.append(r[1])
	mxpoints.append(r[2])
	mypoints.append(r[3])
        mr = sqrt(r[2]*r[2] + r[3]*r[3])
        dth = atan2(r[3],r[2]) - atan2(r[1],r[0])
        rmxpoints.append(mr*cos(dth))
        rmypoints.append(mr*sin(dth))
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1,t+0.5*h)
        k3 = h*f(r + 0.5*k2,t+0.5*h)
        k4 = h*f(r + k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6.0

M2xn = [x/1.496e11 for x in M2xpoints]
M2yn = [y/1.496e11 for y in M2ypoints]

mxn = [x/1.496e11 for x in mxpoints]
myn = [y/1.496e11 for y in mypoints]

rmxn = [x/1.496e11 for x in rmxpoints]
rmyn = [y/1.496e11 for y in rmypoints]

subplot(1,2,1) #inertial frame
xlim(-1.5,1.5)
ylim(-2.5,2.5)
massesx = [0.0]
massesy = [0.0]
plot(massesx,massesy,'go')
plot(M2xn, M2yn, 'r-')
plot(mxn, myn, 'b-')
xlabel("x")
ylabel("y")

subplot(1,2,2) #corotating frame
plot(rmxn, rmyn, 'b-')
xlim(-1.5,1.5)
ylim(-2.5,2.5)
massesx = [0.0]
massesy = [0.0]
plot(massesx,massesy,'go')
massesx = [1.0]
massesy = [0.0]
plot(massesx,massesy,'ro')
xlabel("x")

show()

