import matplotlib.pyplot as plt
import numpy as np

# .linspace arguments are (start, end, number_of_steps)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = (np.sin(x)-2*np.sin(x)*np.sin(x)*np.sin(x))/(2*np.cos(x)*np.cos(x)*np.cos(x)-np.cos(x))
y[:-1][np.diff(y) < 0] = np.nan

# show grid
plt.grid()

plt.xlabel("\u03B8")
plt.ylabel("$sin(\u03B8)-2sin^3(\u03B8)/2cos^3(\u03B8)-cos(\u03B8)$")

# Set the x and y axis cutoffs
plt.ylim(-10,10)
plt.xlim(-2 * np.pi, 2 * np.pi)

# x_labels in radians
radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
radians = [n * np.pi for n in radian_multiples]
radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']

plt.xticks(radians, radian_labels)

plt.title("L.H.S Side Graph", fontsize=14)
plt.plot(x, y)
plt.show()