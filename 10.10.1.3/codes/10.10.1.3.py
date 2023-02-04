import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/home/pratik/CoordGeo')

from line.funcs import *
from conics.funcs import *

O = np.array([[0],[0]])
P = np.array([[0],[5]])
d = 12

m = O - P
n = np.array([[0,1],[-1,0]]) @ m
n = n/np.linalg.norm(n)

coeff_0 = (n.T@n)[0][0]
coeff_1=(2* (n.T@(P-O)))[0][0]
coeff_2 = ((P-O).T @ (P-O) - d**2)[0][0]

coeff = [coeff_0,coeff_1,coeff_2]

l1,l2 = np.roots(coeff)
print(coeff)
print(l1,l2)

Q = P + l1*n

dist = np.linalg.norm(P-Q)

print(dist)


##PLOT
plt.figure(figsize= (22,12))

c1 = circ_gen(O.T,5)
plt.plot(c1[0],c1[1])

tan = line_gen(P,Q)
plt.plot(tan[0],tan[1])

line_1 = line_gen(O,P)
plt.plot(line_1[0],line_1[1])

line_2 = line_gen(O,Q)
plt.plot(line_2[0],line_2[1])

points = np.hstack((O,P,Q))

plt.scatter(points[:][0],points[:][1])

plt.text(O[0]-0.5,O[1],'O')
plt.text(P[0]+0.2,P[1],'P')
plt.text(Q[0]+0.2,Q[1],'Q')

plt.grid()

plt.xlim((-6,12))
plt.ylim((-6,6))
plt.show()

