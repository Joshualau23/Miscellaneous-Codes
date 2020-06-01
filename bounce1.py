# program to follow motion of dropped ball
from numpy import arange, zeros
from pylab import plot, show

# gravity, spring constant
g = 9.81
k = 10.0
k2 = 1000.0
c = 8.0

# ball properties
m = 1.0
r = 0.3

# set initial values

z = 10.0
vz = 0.0
az = 0

t = 0.0
dt = 0.0005
tmax = 10

ts = arange(0,tmax,dt)
N = len(ts)
zs = zeros(N, float)
vzs = zeros(N, float)
azs = zeros(N, float)

# advance motion, Euler method

i = 0
for t in arange(0,tmax,dt):
    F = -g*m          # downwards
    if(z < r):
        F += k*(r-z)  # elastic force
        F -= c*vz     # damping force
        if(z > 0):
            rdef = (r-z)/r # relative deformation; force should get big as this goes to 1
            hrd = rdef/(1.0 - rdef)
            F += k2*hrd*hrd*hrd # hard elastic force
    az = F/m

    z += vz*dt
    vz += az*dt
    ts[i] = t
    zs[i] = z
    vzs[i] = vz
    azs[i] = az
    i = i+1

plot(ts,zs)
show()
