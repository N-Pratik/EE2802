import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'/home/pratik/CoordGeo')

from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

A = np.array([[-1],[1]])
B = np.array([[-1],[-1]])
C = np.array([[1],[-1]])
D = np.array([[1],[1]])

O = (A + C)/2
r = np.linalg.norm((A-C)/2)

c1 = circ_gen(O.T,r)

l_AB = line_gen(A,B)
l_BC = line_gen(B,C)
l_AC = line_gen(A,C)
l_AD = line_gen(A,D)
l_CD = line_gen(C,D)


plt.plot(l_AB[0],l_AB[1])
plt.plot(l_BC[0],l_BC[1])
plt.plot(l_AC[0],l_AC[1])
plt.plot(l_AD[0],l_AD[1])
plt.plot(l_CD[0],l_CD[1])
plt.plot(c1[0],c1[1])

points = np.hstack((A,B,C,D,O))

labels = np.array(['A(-1,-1)','B(-1,-1)','C(1,-1)','D(-1,1)','O(0,0)'])

for i in range(5):
    plt.text(points[0][i]*1.2,points[1][i]*1.1,labels[i])

plt.scatter(points[0],points[1])
plt.show()

