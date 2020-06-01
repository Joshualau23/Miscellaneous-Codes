from numpy import zeros, ones, arange
from pylab import plot, show, scatter, savefig, figure

xp = zeros(1001,float)
yp = zeros(1001,float)

r = arange(3.5,3.7,0.001)
x = ones(len(r))
x = x*0.5

for i in range(1001):
    x = r*x*(1-x)
for i in range(2001):
    x = r*x*(1-x)
    scatter(r,x,s=1)

#figure(num=1, figsize=(2, 2)) 
#savefig("feigen1.png")
figure(figsize=(18, 12), dpi=400)
savefig("myplot.png", dpi = 400)



