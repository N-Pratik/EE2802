import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/home/pratik/CoordGeo')

from line.funcs import *
from conics.funcs import *

a = 7
b = 3

O = np.array([[-1*a],[-1*b]])
o =np.linalg.norm(O)
r = np.sqrt(a**2 -b**2)

print(f"Line equation: ||x||\u00b2 +{-2*O.T}x  + {o**2-r**2}")

c1 = circ_gen(np.array([O[0][0],O[1][0]]), r)

plt.figure(figsize=(5,5))
plt.plot(c1[0],c1[1])

plt.plot(O[0][0],O[1][0],'go')
plt.text(O[0][0]+0.2,O[1][0], 'Centre (-a,-b)')
plt.text(O[0][0]+0.2,O[1][0]-0.7, '(-7,-3)')

plt.show()

