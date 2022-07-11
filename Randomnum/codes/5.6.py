import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

X_arr = np.loadtxt("equi.dat", dtype='double')
N_arr = np.loadtxt("gau.dat", dtype='double')

def get_y(A):
    y_arr = A * X_arr + N_arr
    return y_arr

def get_error_prob(y_arr):
    guesses = np.where(y_arr > 0, 1, -1)
    wrong_count = np.sum(guesses != X_arr)
    return wrong_count / guesses.shape[0]

A_vals = np.arange(0, 4.1, 0.2)
error_probs = []

for A in A_vals:
    y_arr = get_y(A)
    error_probs.append(get_error_prob(y_arr))

def Q(A):
    return erfc(A / np.sqrt(2)) / 2

A_range = np.linspace(0, 10)
# A_range = A_vals
theoretical = Q(A_range)

plt.semilogy(A_vals, error_probs, 'o', label='Numerical')
plt.semilogy(A_range, theoretical, '-', label='Theory')
plt.legend()
plt.grid()
plt.xlabel(r"$A$")
plt.ylabel(r"$P_e$")
plt.savefig('../figs/error_ml.png')
plt.show()
