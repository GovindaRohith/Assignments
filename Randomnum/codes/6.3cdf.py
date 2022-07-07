#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp


x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('gausquare.dat',dtype='double')
randvar=np.sqrt(randvar)
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def rootsumofgau(x):
 if(x < 0):
    return 0
 else:
    return 1-mp.exp(-(x**2)/2)
theory=np.vectorize(rootsumofgau,otypes=['double'])
plt.plot(x.T,err,'o')#plotting the CDF
plt.plot(x,theory(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

plt.show() #opening the plot window
