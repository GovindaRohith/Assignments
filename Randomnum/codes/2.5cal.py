import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import math 

  
def f(x):
    return pow(math.e,(-x*x)/2)

x = sy.Symbol("x")
num=2*sy.integrate(f(x), (x,0,np.inf))
print(num/math.sqrt(2*math.pi))
