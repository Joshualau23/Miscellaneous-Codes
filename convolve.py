from numpy import loadtxt,copy
from pylab import hist, show, figure, ylim, plot

# first round
values = loadtxt("raw_probability.txt",float)
#need to be an odd number
#n, bins, patches = hist(values, 31, normed=0, histtype='stepfilled')

# at the moment assumes odd number of data values
imax = len(values)
imid = len(values -1)/2
vc = copy(values)

#for each point
for i in range (0,imax):
    isum = 0
    count = 0
    #convolve with each other point
    for j in range (0,imax):
        #find index of j-ith point
        di = j - i + imid
        # if it is in range, multiply and add
        if (di >= 0) and (di < imax):
            isum += values[j]*values[di]
            count += 1
    # normalize results and save
    vc[i] = isum/sum(values)

vc = vc/max(vc)

#write output to file
f = open('outputfile0', 'w')
for i in range (0,imax):
    f.write(str(vc[i]))
    f.write('\n')
f.close()

# second round
values = loadtxt("outputfile0",float)
#need to be an odd number
#n, bins, patches = hist(values, 31, normed=0, histtype='stepfilled')

# at the moment assumes odd number of data values
imax = len(values)
imid = len(values -1)/2
vc = copy(values)

#for each point
for i in range (0,imax):
    isum = 0
    count = 0
    #convolve with each other point
    for j in range (0,imax):
        #find index of j-ith point
        di = j - i + imid
        # if it is in range, multiply and add
        if (di >= 0) and (di < imax):
            isum += values[j]*values[di]
            count += 1
    # normalize results and save
    vc[i] = isum/sum(values)

vc = vc/max(vc)

#write output to file
f = open('outputfile1', 'w')
for i in range (0,imax):
    f.write(str(vc[i]))
    f.write('\n')
f.close()

# third round
values = loadtxt("outputfile1",float)
#need to be an odd number
#n, bins, patches = hist(values, 31, normed=0, histtype='stepfilled')

# at the moment assumes odd number of data values
imax = len(values)
imid = len(values -1)/2
vc = copy(values)

#for each point
for i in range (0,imax):
    isum = 0
    count = 0
    #convolve with each other point
    for j in range (0,imax):
        #find index of j-ith point
        di = j - i + imid
        # if it is in range, multiply and add
        if (di >= 0) and (di < imax):
            isum += values[j]*values[di]
            count += 1
    # normalize results and save
    vc[i] = isum/sum(values)

vc = vc/max(vc)

#write output to file
f = open('outputfile2', 'w')
for i in range (0,imax):
    f.write(str(vc[i]))
    f.write('\n')
f.close()


