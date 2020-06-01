from math import sqrt
from numpy import array,arange,zeros 
from pylab import plot, show, axis, xlim, ylim

p = array([-0.3,2.0],float)
v = array([+0.5, -0.3],float)
vl = 1.0 # for display

# draw a vertical line
def vline(x):
    ax0,ax1,ay0,ay1 = axis()
    plot([x,x],[ay0,ay1])

# find root of function using binary search; returns x for which fx = 0
# args are xmin, xmax, accuracy
def findroot(fx,args):
    x1 = args[0]
    x2 = args[1]
    accuracy = args[2]
    f1 = fx(x1)
    f2 = fx(x2)
    if (f1*f2) > 0:
        print "wrong range"
        return -99.0
    else: 
        while abs(x2-x1) > accuracy:
            xm = (x1+x2)/2.0
            fm = fx(xm)
            if fm == 0:
                return xm
            elif (f1*fm) < 0:
                x2 = xm
            else:
                x1 = xm
        return xm

# find tangent vector
def tangent(f,args):
    x = args[0]
    width = args[1]
    x1 = x - width/2.0
    x2 = x + width/2.0
    y1 = f(x1)
    y2 = f(x2)
    dx = x2-x1
    dy = y2-y1
    norm = sqrt(dx*dx +dy*dy)
    tx = dx/norm
    ty = dy/norm
    return tx,ty

# find normal vector
def normal(f,args):
    x = args[0]
    width = args[1]
    x1 = x - width/2.0
    x2 = x + width/2.0
    y1 = f(x1)
    y2 = f(x2)
    dx = (x2-x1)
    dy = (y2-y1)
    norm = sqrt(dx*dx +dy*dy)
    nx = -dy/norm
    ny = dx/norm
    return nx,ny


# defines ray; returns y along v from p, given x
def ray(x):
    return p[1]  + v[1]*(x - p[0])/v[0] 

# defines reflecting surface
def fcall(x):
    a = 0.7
    b = 0.1
    c = 1.0
    return a*x*x + b*x + c

# calculate reflecting surface
nsamples = 1000
xs = arange(-5, 5, (1.0/nsamples))
f = zeros(len(xs),float)
for i in range(len(xs)):
    f[i] = fcall(xs[i])

# plot source position
psz = 8.0            # symbol size
offst = psz/12/72.0   # symbol offset to centre properly
plot(p[0],p[1]-offst,'bo',ms=psz)

# plot source direction
# plot([p[0],p[0]+vl*v[0]],[p[1],p[1]+vl*v[1]])

# plot reflecting surface
plot(xs,f) 

#solve for intersection

# defines distance between ray and surface
def dist(x):
    return fcall(x) - ray(x)

args = [-1.0,10.0,0.01]
xi = findroot(dist,args)
yi = fcall(xi)

# plot intersection point and connect points
plot(xi,yi-offst,'go',ms=psz)
plot([p[0],xi],[p[1],yi])

# calculate tangent vector at intersection point
dx = 0.01
args = [xi,dx] # xposition, width to sample
tx, ty = tangent(fcall,args)
print tx, ty
vl = 1.0
# plot tangent
# plot([xi,xi+vl*tx],[yi,yi+vl*ty])

# now calculate normal vector at intersection point
dx = 0.01
args = [xi,dx] # xposition, width to sample
nx, ny = normal(fcall,args)
print nx, ny
vl = 1.0
# plot normal
plot([xi,xi+vl*nx],[yi,yi+vl*ny])

# now calculate reflected vector
# incident vector is equal to vt + vn
# normal component is equal to vn = (v*n) n_hat
vnn = (v[0]*nx + v[1]*ny)
vn = (vnn*nx, vnn*ny)
vl = 1.0
# plot normal component
# plot([xi,xi+vl*vn[0]],[yi,yi+vl*vn[1]])

# tangential component is vt = v - vn
# reflected vector is equal to vt - vn = v - 2*vn
vr = (v[0] - 2.0*vn[0], v[1] - 2.0*vn[1])
vl = 5.0
plot([xi,xi+vl*vr[0]],[yi,yi+vl*vr[1]])

xlim(-3,3)
ylim(0,5)
show()
