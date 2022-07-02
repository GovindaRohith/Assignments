from more_itertools import sample
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

simlen = 1000000
sample = np.loadtxt('custom.dat',dtype='double')


x = np.linspace(-5,5,40)
CF=[]
for i in range(0,40):
	CF_ind = np.nonzero(sample < x[i]) 
	CF_n = np.size(CF_ind)
	CF.append(CF_n/simlen) 

def g(x) :
   return (1-mp.exp(-x/2))

def cdf(x):

   if x<0 :
         return 0
   else:
         return g(x)
         
y=[-3,-2,1,2,3,4]
CDF = np.vectorize(cdf, otypes=['double'])
         
plt.plot(x[0:40].T,CF,"o")
plt.plot(x,CDF(x))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.show()
