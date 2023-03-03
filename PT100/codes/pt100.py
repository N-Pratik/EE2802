import numpy as np
import matplotlib.pyplot as plt

#Loading Training Data
data = np.loadtxt("Train_data.txt")
T =data[:,[0]]
V = data[:,1]

X = np.hstack((np.ones((data.shape[0],1)),T))

#Regression
A,B = np.linalg.lstsq(X,V, rcond = None)[0]
n = np.array([[A],[B]])
print(n)

#Error Calculation
V_est = (A + B*T).T
Error = np.sum((V-V_est)**2)/data.shape[0]
print(f'Training Mean Error:{Error}')

#PLOTS
x_ax = np.linspace(20,100,2)
y_ax = A + B*x_ax

plt.plot(x_ax,y_ax)
plt.scatter(T,V,color='red')
plt.savefig('Training.png')

###TEST###

test = np.loadtxt('Test_data.txt')

T_test = test[:,0]
V_test = test[:,1]

#Error Calculation
V_est = (A + B*T_test)
Error = np.sum((V_test-V_est)**2)/test.shape[0]
print(f'Training Mean Error:{Error}')

#PLOTS
plt.plot(x_ax,y_ax)
plt.scatter(test[:,0],test[:,1],color='red')
plt.savefig("Test.png")