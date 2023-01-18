import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import sys
sys.path.insert(0,'/home/pratik/CoordGeo')

from line.funcs import *

A = np.array([[1],[2],[3]])
B = np.array([[-1],[0],[0]])
C = np.array([[0],[1],[2]])


m1 = A -B
m2 = C -B

angle = np.arccos((np.matmul(m1.T,m2))/(np.linalg.norm(m1)*np.linalg.norm(m2)))

print(angle)

S1 = np.hstack((A,B))
S2 = np.hstack((C,B))
S3 = np.hstack((C,A))


fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(S1[0], S1[1], S1[2])
ax.plot(S1[0],S1[1],S1[2])

ax.scatter(S2[0], S2[1], S2[2])
ax.plot(S2[0],S2[1],S2[2])

ax.scatter(S3[0], S3[1], S3[2])
ax.plot(S3[0],S3[1],S3[2])


plt.grid()

ax.text(A[0][0],A[1][0],A[2][0],'A')
ax.text(B[0][0],B[1][0],B[2][0],'B')
ax.text(C[0][0],C[1][0],C[2][0],'C')
plt.show()
