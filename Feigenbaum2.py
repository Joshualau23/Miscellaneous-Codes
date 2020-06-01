from numpy import zeros, ones, arange
from pylab import plot, show, scatter

xp = zeros(1001,float)
yp = zeros(1001,float)

r = arange(1.0,4.0,0.01)
x = ones(len(r))
x = x*0.5

for i in range(1001):
    x = r*x*(1-x)
for i in range(1001):
    x = r*x*(1-x)
    scatter(r,x,s=1)
show()



