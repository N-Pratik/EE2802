import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, '/home/pratik/CoordGeo')

#local imports
from line.funcs import *

import matplotlib.pyplot as plt

x = np.linspace(-4,4,200)
z = 0*x

A = np.array([[-1],[-2]])
B = np.array([[3.5],[7]])

x_AB = line_gen(A,B)

plt.plot(x_AB[0],x_AB[1])

plt.plot(x,z)

plt.plot(A[0],A[1],'bo')
plt.text(A[0]+0.2,A[1],'(h,k)')
plt.text(A[0]+0.2,A[1]-0.6,'(-1,-2)') 

plt.plot(B[0],B[1],'bo')
plt.text(B[0]+0.2,B[1],'(x\u2081,y\u2081)')
plt.text(B[0]+0.2,B[1]-0.6,'(3.5,7)') 

plt.text(4,0,'x-axis')
plt.show()
