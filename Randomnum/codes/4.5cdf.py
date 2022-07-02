#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('tri.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def tri_cdf(x):
    if(x>=0 and x<=1):
    	return x*x/2
    elif (x>1 and x<=2):
        return 1-(x-2)*(x-2)/2
    elif (x>2):
    	return 1
    else:
        return 0
theory=np.vectorize(tri_cdf,otypes=['double'])

plt.plot(x.T,err,'o')#plotting the CDF
plt.plot(x,theory(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical", "Theory"])

plt.show() #opening the plot window
