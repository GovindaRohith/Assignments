import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
  
def f(x):
    return 2*(10-x)*(64+10*sy.exp(-2*x))
  
x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, 10))-80*80)
