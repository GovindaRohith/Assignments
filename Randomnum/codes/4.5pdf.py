#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt



maxrange=50
maxlim=6
x = np.linspace(-maxlim+2,6,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
uni1=np.loadtxt('uni1.dat',dtype="double",max_rows=1)
uni2=np.loadtxt('uni2.dat',dtype="double",max_rows=1)
#tri = np.random.normal(0,1,simlen)
tri=np.convolve(uni1,uni2,mode='full')
#print(tri)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(tri < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list


def tri_cdf(x):
    if(x>=0 and x<1):
    	return x
    elif(x==1):
     	return 1
    elif (x>1 and x<=2):
        return 2-x
    else:
        return 0
theory=np.vectorize(tri_cdf,otypes=['double'])
plt.plot(x[0:(maxrange-1)],pdf)
#plt.plot(x,theory(x))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])


plt.show() #opening the plot window

