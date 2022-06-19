import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
  
def f(x):
    return 8
  
x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, 10)))
