import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

import sys
sys.path.insert(0,'/home/pratik/CoordGeo')

from line.funcs import *

A = np.array([[2],[3]])
B = np.array([[4],[-1]])
C = np.array([[1],[2]])

m = B-C
n = np.array([[1,0],[0,-1]]) @ m

# EQUATION of ALTITUDE

c = m.T@A
print(f"altitude eq: {m.T}x = {c}")

mu = cp.Variable()

prob = cp.Problem(cp.Minimize(cp.norm(A-B-mu*m)))
prob.solve()

print(f"Alt_Len={prob.value}")

D = B + mu.value*m

print(f"POI:{D}")

#PLOTTING

l1 = line_gen(A,B)
l2 = line_gen(B,C)
l3 = line_gen(C,A)
l4 = line_gen(A,D)

plt.plot(l1[0,:],l1[1,:],label='$AB$')
plt.plot(l2[0,:],l2[1,:],label='$BC$')	
plt.plot(l3[0,:],l3[1,:],label='$CA$')
#plt.plot(l4[0,:],l4[1,:],label='$AD$')

plt.scatter(A[0],A[1])
plt.scatter(B[0],B[1])
plt.scatter(C[0],C[1])
plt.scatter(D[0],D[1])

plt.text(A[0]*(1+0.1),A[1]*(1),'A')
plt.text(B[0]*(1),B[1]*(1-0.1),'B')
plt.text(C[0]*(1),C[1]*(1-0.1),'C')


plt.grid()
plt.savefig('../figs/figure_1.png')
plt.show()
