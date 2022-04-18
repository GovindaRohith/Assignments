import numpy as np
tan1 = [17,20*np.sqrt(17),100] #quadratic equation to find intersection of y=2x+√(17) and hyperbola
rts = np.roots(tan1) #roots
point1[0]=rts[0]
#using the equation of the line
point1[1]=2*rts[0]+np.sqrt(17)


tan1 = [17,-20*np.sqrt(17),100] #quadratic equation to find intersection of y=2x-√(17) and hyperbola
rts = np.roots(tan1) #roots
point2[0]=rts[0]
#using the equation of the line
point2[1]=2*rts[0]-np.sqrt(17)

print("The first point of contact is ({},{})".format(point1[0],point1[1]))
print("The second point of contact is ({},{})".format(point2[0],point2[1]))