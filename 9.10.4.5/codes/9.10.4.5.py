import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/home/pratik/CoordGeo')

from line.funcs import *
from conics.funcs import *


O = np.array([[5],[0]])
B = np.array([[0],[0]])
r = 5
r2 =6


c1 = circ_gen(O.T,r)
c2 = circ_gen(B.T,r2)

plt.plot(c1[0],c1[1])
plt.plot(c2[0],c2[1])

plt.plot(O[0],O[1],'bo')
plt.plot(B[0],B[1],'bo')


plt.text(O[0],O[1],'O (5,0)')
plt.text(B[0],B[1],'B (0,0)')


plt.grid()
plt.show()
