import numpy as np 
import matplotlib.pyplot as plt

#Loading Training Data
data = np.loadtxt("Train_data.txt")
T =data[:,[0]]
V = data[:,1]
X = np.hstack((np.ones((T.shape[0],1)),T))

def cost(n):
    V_est = (X@n).T
    Error = np.sum((V-V_est)**2)/data.shape[0]
    return Error

A = np.arange(75,85,0.1)
B = np.arange(-0.5,0.5,0.01)

Z = np.zeros((A.shape[0],B.shape[0]))

for i,x_ax in enumerate(A):
            for j,y_ax in enumerate(B):
                            Z[i][j] = cost(np.array([[x_ax],[y_ax]]))

x = range(100)
fig = plt.figure().add_subplot(111,projection='3d')
X,Y = np.meshgrid(x,x)

my_col = plt.cm.jet(Z/np.amax(Z))
fig.plot_surface(X,Y,Z, facecolors = my_col)

#plt.imshow(Z,cmap='gray')
#print(np.min(Z))
plt.show()

