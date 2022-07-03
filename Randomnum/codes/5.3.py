import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
simlen = 1000000
randvar=np.loadtxt('./gau.dat',dtype='double')
x = range(simlen)
plt.plot(x,randvar)
plt.grid() 
plt.xlabel('numbers')
plt.ylabel('Y')
plt.show()
