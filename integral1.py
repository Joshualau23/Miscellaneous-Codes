from numpy import arange, sin, pi, cos
from pylab import plot, show, ylim, savefig

#define the function to approximate
def f_of_x(x):
    return cos(x*x)/(1+x*x)

#global plot limits
ylim (-1.1, 1.1)

#first approximation: one rectangle

#define left and right limits and midpoint
ll = -5.0
rl = +5.0
mp = (ll + rl)/2.0

#set the x and y values
x = arange(ll,rl,0.01)
y = f_of_x(x)

#plot the function
plot(x,y,color = 'b')
#plot the x-axis
plot([1.1*ll,1.1*rl],[0,0],color='k')
#plot the top of the rectangle
plot([ll,rl],[f_of_x(mp),f_of_x(mp)],color='g')
#plot the sides of the rectangle
plot([ll, ll], [0, f_of_x(mp)], color='g')
plot([rl, rl], [0, f_of_x(mp)], color='g') 

show()

###########################################################

#second approximation: two rectangles


#define left and right limits and midpoint
ll = -5.0
rl = 0.0
mp = (ll + rl)/2.0

#set the x and y values
x = arange(ll,rl,0.01)
y = f_of_x(x)

#plot the function
plot(x,y,color = 'b')
#plot the x-axis
plot([1.1*ll,1.1*rl],[0,0],color='k')
#plot the top of the rectangle
plot([ll,rl],[f_of_x(mp),f_of_x(mp)],color='g')
#plot the sides of the rectangle
plot([ll, ll], [0, f_of_x(mp)], color='g')
plot([rl, rl], [0, f_of_x(mp)], color='g') 

#define left and right limits and midpoint
ll = 0.0
rl = 5.0
mp = (ll + rl)/2.0

#set the x and y values
x = arange(ll,rl,0.01)
y = f_of_x(x)

#plot the function
plot(x,y,color = 'b')
#plot the x-axis
plot([1.1*ll,1.1*rl],[0,0],color='k')
#plot the top of the rectangle
plot([ll,rl],[f_of_x(mp),f_of_x(mp)],color='g')
#plot the sides of the rectangle
plot([ll, ll], [0, f_of_x(mp)], color='g')
plot([rl, rl], [0, f_of_x(mp)], color='g') 

show()

###########################################################

