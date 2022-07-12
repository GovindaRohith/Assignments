import numpy as np
import mpmath as mp
import scipy
import math as mk
import matplotlib.pyplot as plt


maxrange=50
maxlim=11.0
x = np.linspace(0,maxlim,maxrange)#points on the x axis
xx = np.linspace(0,maxlim,maxrange*50) #more points on the x axis

a = []

for i in range(1,11):
	a.append(i*1)
 
def proberr2(x):
	return 1/2*(1-mk.sqrt(x/(x+2)))

vec_proberr2 = np.vectorize(proberr2, otypes=[np.float])

plt.semilogy(np.array(a), np.loadtxt('cp7.dat',dtype='double',max_rows=10),'o') #plotting proberr graph
plt.semilogy(xx,vec_proberr2(xx))

plt.grid() #creating the grid
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Numerical","Theory"])

plt.show() #opening the plot window
