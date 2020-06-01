# step 0
from math import cos,sin,pi
from numpy import array,arange,sin,cos,linspace,zeros
from pylab import plot,show,ylim

#x = arange(0,pi,pi/100.0)
#plot(x,sin(x))
#show()

#step 1

from math import cos,sin,pi
from numpy import arange,sin,cos
from pylab import plot,show

closedint = range(101) # 0 to 100, so 101 values 
x = (pi/100)*array(closedint,float)


#plot(x,sin(x))
#ylim(0.0,1.1)
#show()

#step 2
xt = 1.1
yt = sin(xt)
dx = 0.3
dy = dx*cos(xt)

tangx = array([xt -dx,xt,xt+dx],float)
tangy = array([yt-dy,yt,yt+dy],float)
#plot(tangx,tangy,'k-')
#show()

#step 3
#plot(x,cos(x))
#ylim(-1.1,1.1)
#show()

#plot(xr,cos(xr),'ko')

#step 4/5

#x = linspace(0,pi,100)

h = pi/100.0
fd = zeros(len(x),float)

for i in range(1,100): # values 1 to 99
    fd[i] = (sin(x[i]+h) - sin(x[i]))/h

xr = x[1:100]
fdr = fd[1:100]

#plot(xr,cos(xr),'ko')
#plot(xr,fdr)
#show()

#step 6
#plot(xr, fdr-cos(xr),'ko')
#show()

#step 7
rd = zeros(len(x),float)
for i in range(1,100): # values 1 to 99
    rd[i] = (sin(x[i]) - sin(x[i]-h))/h

rdr = rd[1:100]

#plot(xr, fdr-cos(xr),'ko')
#plot(xr, rdr-cos(xr),'ko')
#show()

#step 8

cd = zeros(len(x),float)
for i in range(1,100): # values 1 to 99
    cd[i] = (sin(x[i]+h/2) - sin(x[i]-h/2))/h

cdr = cd[1:100]

#plot(xr, fdr-cos(xr),'ko')
#plot(xr, rdr-cos(xr),'ko')
#plot(xr, cdr-cos(xr),'ko')
#show()

#step 9

cd2 = zeros(len(x),float)
for i in range(1,100): # values 1 to 99
    cd2[i] = (sin(x[i]+h) - sin(x[i]-h))/2/h

cd2r = cd2[1:100]

plot(xr, cdr-cos(xr),'ko')
plot(xr, cd2r-cos(xr),'ko')
show()



