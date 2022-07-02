#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib
import mpmath as mp
matplotlib.rcParams['backend'] = 'GTK3Agg'
import matplotlib.pyplot as plt


x = np.linspace(-10,10,50)#points on the x axis
def cdf(x):
  if(x<0):
    return 0
  else:
    p=mp.exp(-x/2)
    return 1-p
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
randvar = -2*np.log(1 - randvar)
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
theory=np.vectorize(cdf,otypes=[float])
#print(theory(x))
plt.plot(x,err,'bo',color="blue")#plotting the CDF
plt.plot(x,theory(x),color="orange")
plt.grid() #creating the grid
plt.xlabel('$v$')
plt.ylabel('$F_V(v)$')
plt.legend(["Numerical", "Theory"])
#plt.savefig('../figs/exp_cdf.png')
plt.show()
