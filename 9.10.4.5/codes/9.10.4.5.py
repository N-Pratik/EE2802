import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/home/pratik/CoordGeo')

from line.funcs import *
from conics.funcs import *


O = np.array([[0],[0]])
B = np.array([[5],[0]])
r = 5








c1 = circ_gen(O,r)

plt.plot(c1[0],c1[1])
plt.grid()
plt.show()
