import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
simlen = 1000000
randvar = np.loadtxt('./gau.dat',dtype='double')


x = np.linspace(-5,5,40)
CF=[]
for i in range(0,40):
	CF_ind = np.nonzero(randvar < x[i]) 
	CF_n = np.size(CF_ind)
	CF.append(CF_n/simlen) 
	
	
def Q(x):
    return (1-mp.erf(x/mp.sqrt(2)))/2
    
def f(x):
    return 1-Q(x)
    
cdf = np.vectorize(f)

plt.plot(x.T,cdf(x))
plt.plot(x[0:40].T,CF,"o")
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Theory","Numerical"])
plt.savefig("../figs/gauss_cdf.pdf")
plt.savefig("../figs/gauss_cdf.eps")
plt.show()
