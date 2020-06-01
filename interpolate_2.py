# 2: linear interpolation over a single interval; 
# this time interpolating function plots as well

from numpy import arange, zeros
from pylab import plot, show, xlim, ylim

#define a routine to return y(x), given data (x0,y0), (x1,y1)
def lin_interp(x0,y0,x1,y1,x):
    y = 0
    P0 = (x1-x)/(x1-x0)
    P1 = (x-x0)/(x1-x0)
    y += y0*P0
    y += y1*P1
    return y

def show_lin_interp(x0,y0,x1,y1):
    dx = (x1-x0)/30.0
    x = arange(0,x1,dx)
    y = zeros(len(x),float)
    for i in range(len(x)):
        y[i] = lin_interp(x0,y0,x1,y1,x[i])
    plot(x,y,'ro')

#set data
x0 = 0.0
x1 = 2.0
y0 = 1.0
y1 = 2.0

#make box a bit larger to show end points
wx = x1-x0
wy = y1-y0
xlim(x0 -0.1*wx, x1+0.1*wx)
ylim(y0 -0.1*wy, y1+0.1*wy)

# plot interpolation between points
show_lin_interp(x0,y0,x1,y1)

#plot end points
xl = [x0,x1]
yl = [y0,y1]
plot(xl,yl,'ko')

show()

