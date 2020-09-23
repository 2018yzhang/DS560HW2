import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('a.csv','r') as xFile:
    xHeader = xFile.readline()
    xList = csv.reader(xFile)
    for row in xList:
        x.append(int(row[0]))

with open('b.csv','r') as yFile:
    yHeader = yFile.readline()
    yList = csv.reader(yFile)
    for row in yList:
        y.append(int(row[0]))

plt.plot(x,y, label='y=3*x+6')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('c.png')