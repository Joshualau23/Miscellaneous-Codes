from numpy import loadtxt,zeros
from pylab import hist, show, figure, ylim, plot
marks = loadtxt("testdata.txt",float)
#print marks
n, bins, patches = hist(marks, 30, normed=0, histtype='stepfilled')

size = len(marks)

# find sensible plot limits
ymax = max(n) + 1
ylim (0, ymax)

#find mean
mmean = sum(marks)/len(marks)
plot([mmean, mmean], [0, ymax], color='k', linestyle='-', linewidth=2)

show()

#calculate all pair averages
psize = size*size
p_av = zeros(psize,float)

for i in range(0,size):
    for j in range(0,size):
        if i != j:
            p_av[(size*i)+j] = (marks[i]+marks[j])/2.0
        else:
            p_av[(size*i)+j] = 0.0

#plot a histogram of them
n2, bins2, patches2 = hist(p_av, 30, normed=0, histtype='stepfilled')
show()

#now try calculating all triplet averages
tsize = size*psize
t_av = zeros(tsize,float)

for i in range(0,size):
    for j in range(0,size):
        if i != j:
            for k in range(0,size):
                if (k != j) and (k!= i):
                    ind = k + (j+(i*size))*size
                    t_av[ind] = (marks[i]+marks[j]+marks[k])/3.0

#plot a histogram of them
n3, bins3, patches3 = hist(t_av, 30, normed=0, histtype='stepfilled')
show()

###now try calculating all quad averages
##qsize = size*size*size*size
##q_av = zeros(qsize,float)
##
##for i in range(0,size):
##    print "doing i = ", i
##    for j in range(0,size):
##        if i != j:
##            for k in range(0,size):
##                if (k != j) and (k!= i):
##                    for l in range(0,size):
##                        if (l != k) and (l!= j) and (l != i):
##                            ind = l + size*(k + (j+(i*size))*size)
##                            q_av[ind] = (marks[i]+marks[j]+marks[k]+marks[l])/4.0
##
##print "done "
###plot a histogram of them
##n4, bins4, patches4 = hist(t_av, 30, normed=0, histtype='stepfilled')
##show()



