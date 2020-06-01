from numpy import array,arange,zeros 
from pylab import plot, show, axis

p = array([0.1,1.0],float)
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

# defines ray; returns y along v from p, given x
def ray(x):
    return p[1]  + v[1]*(x - p[0])/v[0] 

# defines reflecting surface
def fcall(x):
    a = 0.7
    b = 0.1
    return a*x + b

# calculate reflecting surface
nsamples = 1000
xs = arange(-1, 2, (1.0/nsamples))
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

show()
