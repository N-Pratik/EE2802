import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[-1],[0.5],[4]])
B = np.array([[1],[0.5],[4]])
C= np.array([[1],[-0.5],[4]])
D = np.array([[-1],[-0.5],[4]])

m1 = A -B 
m2 = D - C
m3 = C -B
m4 = A - D
fig = plt.figure()
ax =fig.add_subplot(projection='3d')

if m1.all() == m2.all():
    Area= np.linalg.norm(m1)*np.linalg.norm(m3)
    S1 = np.hstack((A,B))
    S2 = np.hstack((C,D))
    S3 = np.hstack((C,B))
    S4 = np.hstack((A,D))

 
elif m1.all == -1*m2.all():
    Area= np.linalg.norm(m1)*np.linalg.norm(m3)
    S1 = np.hstack((A,B))
    S2 = np.hstack((C,D))
    S3 = np.hstack((C,A))
    S4 = np.hstack((B,D))


elif m3.all == m4.all:
    Area = np.linalg.norm(m2)*np.linalg.norm(m3)
    S1 = np.hstack((A,C))
    S2 = np.hstack((C,B))
    S3 = np.hstack((B,D))
    S4 = np.hstack((A,D))

elif m3.all == -1* m4.all:
    Area = np.linalg.norm(m2)*np.linalg.norm(m3)
    S1 = np.hstack((A,D))
    S2 = np.hstack((D,C))
    S3 = np.hstack((C,B))
    S4 = np.hstack((B,A))


ax.scatter(S1[0],S1[1],S1[2])
ax.plot(S1[0],S1[1],S1[2])

ax.scatter(S2[0],S2[1],S2[2])
ax.plot(S2[0],S2[1],S2[2])

ax.scatter(S3[0],S3[1],S3[2])
ax.plot(S3[0],S3[1],S3[2])

ax.scatter(S4[0],S4[1],S4[2])
ax.plot(S4[0],S4[1],S4[2])

ax.text(A[0][0],A[1][0],A[2][0],'A')
ax.text(B[0][0],B[1][0],B[2][0],'B')
ax.text(C[0][0],C[1][0],C[2][0],'C')
ax.text(D[0][0],D[1][0],D[2][0],'D')


print(Area)
plt.grid()
plt.show()
