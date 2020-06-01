from math import sin
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel

a = 0.0
b = 150.0
N = 3000
h = (b-a)/N

sl = 10.0
rl = 28.0
bl = 8.0/3.0

def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sl*(y-x)
    fy = rl*x - y - x*z
    fz = x*y - bl*z
    return array([fx,fy,fz],float)

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

r = array([0.0,1.0,0.0],float)

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	zpoints.append(r[2])
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1,t+0.5*h)
        k3 = h*f(r + 0.5*k2,t+0.5*h)
        k4 = h*f(r + k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6.0

#plot(tpoints, ypoints)
plot(xpoints, zpoints)


xpoints = []
ypoints = []
zpoints = []

r = array([0.0,0.999,0.0],float)

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
	zpoints.append(r[2])
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1,t+0.5*h)
        k3 = h*f(r + 0.5*k2,t+0.5*h)
        k4 = h*f(r + k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6.0

#plot(tpoints, ypoints)
plot(xpoints, zpoints)
xlabel("x")
ylabel("z")
show()

