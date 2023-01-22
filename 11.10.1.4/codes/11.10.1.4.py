import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[7],[6]])

B = np.array([[3],[4]])

Con1 = (2*B.T - 2*A.T)


Res1 = (np.linalg.norm(B)**2 - np.linalg.norm(A)**2)

Con2 = np.array([[0,1]])
Res2 = 0

Con = np.block([[Con1],[Con2]])
Res = np.block([[Res1],[Res2]])

P = np.linalg.inv(Con) @ Res

plt.plot(P[0][0], P[1][0], 'bo')
plt.text(P[0][0]+0.5, P[1][0], 'P')

x = np.linspace(0,10,100)
y= 0*x

plt.plot(x,y)

plt.plot(A[0][0], A[1][0], 'bo')
plt.text(A[0][0]+0.5, A[1][0], 'A')

plt.plot(B[0][0], B[1][0], 'bo')
plt.text(B[0][0]+0.5, B[1][0], 'B')
plt.grid()
print(P)
plt.show()
