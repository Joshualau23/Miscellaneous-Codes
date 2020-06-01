from math import log, sqrt
from numpy import arange, array, ones, zeros
import cmath
from pylab import imshow, show, gray
import time

#xc = -0.7620995
#yc = 0.08898
#xc = 0.27
#yc = 0.0055
xc = 0.0166150025
yc = 1.037767233
scale = 5.0e-9

t0 = time.time()

x = arange(-3.0,2.0,0.002)
y = arange(-2.0,4.0,0.002)

x = scale*x - xc
y = scale*y - yc

in_set = zeros([len(y)+1,len(x)+1],float)

j = 0
for xs in x:
    k = 0
    for ys in y:
        c = xs + ys*1j  
        z = 0 + 0j 
        for i in range(100):
            z = (z*z)+c
            if abs(z) > 2.0:
                in_set[k,j] = log(i+1) - 3
                break
        k += 1
    j += 1
   
imshow(in_set)
#gray()

dt = time.time()
print dt - t0 

show()
    
