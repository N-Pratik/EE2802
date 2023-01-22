import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax =fig.add_subplot(projection='3d')

a1 = np.array([[-1],[-1],[-1]])
b1 = np.array([[7],[-6],[1]]) 

a2 =np.array([[3],[5],[7]])
b2 =np.array([[1],[-2],[1]]) 

b_cross = np.cross(np.array([b1[0][0],b1[1][0],b1[2][0]]),np.array([b2[0][0],b2[1][0],b2[2][0]])) 

dist = abs(b_cross.T @ (a2-a1))/np.linalg.norm(b_cross)

print(dist)

c1 = a1 + 5*b1
c2 = a2 + 5*b2

d1 = a1 - 5*b1
d2 = a2 - 5*b2


l1 = np.hstack((d1,c1))
ax.plot(l1[0],l1[1])

l2 = np.hstack((d2,c2))
ax.plot(l2[0],l2[1])

plt.grid()
plt.show()
