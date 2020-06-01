# demonstrate that the interpolation of transformed points is equal to 
# the transformation of the interpolation

from rotatepoints import rotatepoints
from math import pi

from numpy import arange, zeros, loadtxt
from pylab import plot, show, xlim, ylim

def lin_interp(x0,y0,x1,y1,x):
    y = 0
    P0 = (x1-x)/(x1-x0)
    P1 = (x-x0)/(x1-x0)
    y += y0*P0
    y += y1*P1
    return y

def cube_interp(x0,y0, x1,y1, x2,y2, x3,y3, x):
    y = 0.0
    P0 = (x-x1)*(x-x2)*(x-x3)/(x0-x1)/(x0-x2)/(x0-x3)
    P1 = (x-x0)*(x-x2)*(x-x3)/(x1-x0)/(x1-x2)/(x1-x3)
    P2 = (x-x0)*(x-x1)*(x-x3)/(x2-x0)/(x2-x1)/(x2-x3)
    P3 = (x-x0)*(x-x1)*(x-x2)/(x3-x0)/(x3-x1)/(x3-x2)
    y += y0*P0
    y += y1*P1
    y += y2*P2
    y += y3*P3
    return y


def show_lin_interp(x0,y0,x1,y1):
    x = arange(x0,x1,(x1-x0)/100.0)
    y = zeros(len(x),float)
    for i in range(len(x)):
        y[i] = lin_interp(x0,y0,x1,y1,x[i])
    plot(x,y,'r-')

def show_param_cube_interp(x0,y0, x1,y1, x2,y2, x3,y3):
    t = arange(0.0,1.0,1.0/300.0)
    x = zeros(len(t),float)
    y = zeros(len(t),float)
    for i in range(len(x)):
        x[i] = cube_interp(0.0,x0,(1.0/3.0),x1,(2.0/3.0),x2,1.0,x3,t[i])
        y[i] = cube_interp(0.0,y0,(1.0/3.0),y1,(2.0/3.0),y2,1.0,y3,t[i])
    plot(x,y,'r-')

#connect the dots

xr, yr = loadtxt("pk_dat.txt",float,unpack=True)

angle = 45.0

# draw the original + rotated outlines
for angle in range(0,360,60):
    theta = angle/180.0*pi
    xs, ys = rotatepoints(xr,yr,theta)
    #plot(xs,ys,'ko')
    N = len(xs)
    for i in range (0,N-3,3):
        show_param_cube_interp(xs[i],ys[i],xs[i+1],ys[i+1],xs[i+2],ys[i+2],xs[i+3],ys[i+3])

# draw the face
if 1:
    xs, ys = loadtxt("pk2_dat.txt",float,unpack=True)
    N = len(xs)
    for i in range (N-1):
        show_lin_interp(xs[i],ys[i],xs[i+1],ys[i+1])

    xs, ys = loadtxt("pk3_dat.txt",float,unpack=True)
    N = len(xs)
    for i in range (N-1):
        show_lin_interp(xs[i],ys[i],xs[i+1],ys[i+1])

    xs, ys = loadtxt("pk4_dat.txt",float,unpack=True)
    N = len(xs)
    for i in range (N-1):
        show_lin_interp(xs[i],ys[i],xs[i+1],ys[i+1])

# default window seems to be 15x12?
# so rescale to get ~square aspect ratio
xlim(-15,15.0)
ylim(-12.0,12.0)

#display the result
show()
