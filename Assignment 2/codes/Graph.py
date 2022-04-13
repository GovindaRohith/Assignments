import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
x = np.linspace(-9, 9,1000)
y = np.linspace(-9, 9,1000)
x, y = np.meshgrid(x, y)
axes()
hy=plt.contour(x, y,(3*x*x-5*y*y), [15], colors='black')
h1,_=hy.legend_elements()
tan1=plt.contour(x, y,(y-2*x), [np.sqrt(17)], colors='blue')
h2,_=tan1.legend_elements()
tan2=plt.contour(x, y,(y-2*x), [-np.sqrt(17)], colors='red',linestyles='solid')
h3,_=tan2.legend_elements()
plt.legend([h1[0],h2[0],h3[0]],["Hyperbola","y=2x+√(17)","y=2x-√(17)"])
plt.grid()
plt.show()