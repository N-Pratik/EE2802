import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,200)
y= 2*x
z = 0*x

plt.plot(x,y)
plt.plot(x,z)

plt.plot(2,4,'bo')
plt.text(2.2,4,'(h,k)')
plt.text(2.2,3.4,'(2,4)') 

plt.plot(3.5,7,'bo')
plt.text(3.7,7,u'(x\u2081,y\u2081)')
plt.text(3.7,6.4,'(3.5,7)')

plt.text(4,0,'x-axis')
plt.show()
