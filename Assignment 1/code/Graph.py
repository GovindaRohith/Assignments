import matplotlib.pyplot as plt
import numpy as np

# .linspace arguments are (start, end, number_of_steps)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = (np.sin(x)-2*np.sin(x)*np.sin(x)*np.sin(x))/(2*np.cos(x)*np.cos(x)*np.cos(x)-np.cos(x))
y[:-1][np.diff(y) < 0] = np.nan



plt.xlabel("\u03B8")
plt.ylabel("y")

# Set the x and y axis cutoffs
plt.ylim(-10,10)
plt.xlim(-2 * np.pi, 2 * np.pi)

# x_labels in radians
radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
radians = [n * np.pi for n in radian_multiples]
radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']

plt.xticks(radians, radian_labels)

plt.plot(x, y,color='red',label="L.H.S")
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)
y[:-1][np.diff(y) < 0] = np.nan
plt.plot(x,y,linestyle='dashed',color='blue',linewidth='3',label='R.H.S')
plt.legend(loc="upper left")
plt.show()
