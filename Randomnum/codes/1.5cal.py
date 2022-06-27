import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
  
  
def f(x):
    return x
def g(x):
    return x*x;
x = sy.Symbol("x")
print("E(U)=",sy.integrate(f(x), (x, 0, 1)))
print("E(U^2)=",sy.integrate(g(x), (x, 0, 1)))
print("Variance=",(sy.integrate(g(x), (x, 0, 1))-sy.integrate(f(x), (x, 0, 1))*sy.integrate(f(x), (x, 0, 1))))
