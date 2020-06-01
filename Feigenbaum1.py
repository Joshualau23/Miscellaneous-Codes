from numpy import zeros, arange
from pylab import plot, show, scatter

r = 1.0
x = 0.5

xp = zeros(1001,float)
yp = zeros(1001,float)

for r in arange(1.0, 4.0, 0.01):
    for i in range(1001):
        x = r*x*(1-x)
    for i in range(1001):
        x = r*x*(1-x)
        yp[i] = x
        xp[i] = r
    #plot(xp,yp,"k.")
    scatter(xp,yp,s=1)
show()



