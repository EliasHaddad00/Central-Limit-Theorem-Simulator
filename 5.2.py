import math
import numpy as np
import re
import scipy.stats as st
import matplotlib.pyplot as plt

x = 1000
a = 24693
c = 3967
K = 2**17

uVal = []
count = 0
itterations = 300000
while count < itterations:

    x = (a * x + c) % K
    uVal.append(x / K)

    count = count + 1
with open('uVal.txt', 'w') as file:
    file.write('\n'.join(str(value) for value in uVal))
#for i in uVal:
#    print(i)

mN = [10, 30, 50, 100, 150, 250, 500, 1000]
results = []
mean =  71.438090582  # mean
sigma = 37.34277352  # sqrt of var

fp = open("estimates/n=10.txt", 'r')
lines = fp.readlines()
n10 = []
for i in range(0, len(lines)):
    someString=str(lines[i][5:-2])
    n10.append(someString)

fp = open("estimates/n=30.txt", 'r')
lines = fp.readlines()
n30 = []
for i in range(0, len(lines)):
    someString=str(lines[i][5:-2])
    n30.append(someString)

fp = open("estimates/n=50.txt", 'r')
lines = fp.readlines()
n50 = []
for i in range(0, len(lines)):
    someString=str(lines[i][5:-2])
    n50.append(someString)

fp = open("estimates/n=100.txt", 'r')
lines = fp.readlines()
n100 = []
for i in range(0, len(lines)):
    someString=str(lines[i][6:-2])
    n100.append(someString)

fp = open("estimates/n=150.txt", 'r')
lines = fp.readlines()
n150 = []
for i in range(0, len(lines)):
    someString=str(lines[i][6:-2])
    n150.append(someString)

fp = open("estimates/n=250.txt", 'r')
lines = fp.readlines()
n250 = []
for i in range(0, len(lines)):
    someString=str(lines[i][6:-2])
    n250.append(someString)

fp = open("estimates/n=500.txt", 'r')
lines = fp.readlines()
n500 = []
for i in range(0, len(lines)):
    someString=str(lines[i][6:-2])
    n500.append(someString)

fp = open("estimates/n=1000.txt", 'r')
lines = fp.readlines()
n1000 = []
for i in range(0, len(lines)):
    someString=str(lines[i][7:-2])
    n1000.append(someString)

def zscore(mn, n):
    global mean
    global sigma
    return ((mn - mean) / (sigma * math.sqrt(n)))

#n10-n1000 lists are read in from 4.2 files
for n in mN:
    print(n)
    for iid in range(0, 110):
        count = 0
        tempResults = []
        if n==10:
            Q=float(n10.pop(0))
            results.append((n,zscore(Q,n))) #finding z-score using formula
        if n==30:
            Q=float(n30.pop(0))
            results.append((n,zscore(Q,n)))
        if n==50:
            Q=float(n50.pop(0))
            results.append((n,zscore(Q,n)))
        if n==100:
            Q=float(n100.pop(0))
            results.append((n,zscore(Q,n)))
        if n==150:
            Q=float(n150.pop(0))
            results.append((n,zscore(Q,n)))
        if n==250:
            Q=float(n250.pop(0))
            results.append((n,zscore(Q,n)))
        if n==500:
            Q=float(n500.pop(0))
            results.append((n,zscore(Q,n)))
        if n==1000:
            Q=float(n1000.pop(0))
            results.append((n,zscore(Q,n)))

    ycord = [pair[1] for pair in results]

    print("Average: ", np.mean(ycord))
    print("Sqrt of Standard Deviation: ", math.sqrt(np.std(ycord)))

    #reading z-values into a file to archive
    if(n==10):
        with open('z-values/Zn=10.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))
    if (n == 30):
        with open('z-values/Zn=30.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))
    if (n == 50):
        with open('z-values/Zn=50.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))
    if (n == 100):
        with open('z-values/Zn=100.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))
    if (n == 150):
        with open('z-values/Zn=150.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))
    if (n == 250):
        with open('z-values/Zn=250.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))
    if (n == 500):
        with open('z-values/Zn=500.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))
    if (n == 1000):
        with open('z-values/Zn=1000.txt', 'w') as file:
            file.write('\n'.join(str(value) for value in ycord))

    points = [0, 0, 0, 0, 0, 0, 0]
    zValues = [1.4, 1, 0.5, 0, -0.5, -1, -1.4]
    for point in ycord:
        if(point <= 1.4):
            points[0] += 1
        if(point <= 1.0):
            points[1] += 1
        if(point <= 0.5):
            points[2] += 1
        if(point <= 0):
            points[3] += 1
        if(point <= -0.5):
            points[4] += 1
        if(point <= -1):
            points[5] += 1
        if(point <= -1.4):
            points[6] += 1

    for i in range(0, len(points)):
        points[i] = points[i] / 880  # gettins=g probability
        #print("points:",points[i])
    empericalCDF = []
    for i in range(0, len(points)):
        print("The probability of " +
              str(zValues[i]) + " is: " + str(points[i]))
        empericalCDF.append((zValues[i], points[i]))

    madnValues = []
    cdfValue = [0.9192, 0.8413, 0.6915, 0.5, 0.3085, 0.1587, 0.0808] #real z-score
    for i in range(0, len(points)):
        madnValues.append(np.abs(points[i] - cdfValue[i]))
        print("madn:",madnValues)


    MADn = np.amax(madnValues)
   # MADn=madnValues.pop(0)
    print("what is this",zValues[np.argmax(madnValues)])
    MADnPlot = (zValues[np.argmax(madnValues)], MADn)
    print("The max value for MADn = " + str(MADn))

    #calculating z score from -2.5 to 2.5
    plotCDF = []
    start = -2.5
    while start <= 2.5:
        plotCDF.append((start, st.norm.cdf(start)))
        start += 0.01

    plt.title('Graph fit of standard normal CDF for n = ' + str(n))
    plt.plot(*zip(*plotCDF), label='Standard Normal CDF')
    plt.scatter(*zip(*empericalCDF), color='green', label='Emperical CDF')
    plt.scatter(*MADnPlot, color='red', label=r'$MAD_n$')
    # plt.axhline(np.mean(ycord), color='black')
    plt.ylabel(r'$M_n(x)$')
    plt.xlabel(r'$n$')
    plt.legend()
    plt.show()