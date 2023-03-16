import numpy as np 
import matplotlib.pyplot as plt

#Loading Training Data
data = np.loadtxt("Train_data.txt")
T =data[:,[0]]
V = data[:,1]
X = np.hstack((np.ones((T.shape[0],1)),T))

learn_rate = 472e-7
tolerance = 1

A= np.random.rand()
B= np.random.rand() 
n = np.array([[A],[B]])

def cost(n):
    V_est = (X@n).T
    Error = np.sum((V-V_est)**2)/data.shape[0]
    return Error

itr = 0
while (cost(n) > tolerance) and (itr<1e+10):
    itr += 1
    n -= learn_rate*(((X@n).T-V)@X).T

print(f"iterations taken:{itr}")
print(f"n:{n}")
print(f"Error={cost(n)}")

#PLOTS

x = np.linspace(20,110,50)
y = n[0] + n[1]*x

plt.plot(x,y)
plt.scatter(T.T,V, color = 'red')
plt.savefig('../figs/Training_GD.png')
plt.clf()

test = np.loadtxt('Test_data.txt')

T_test = test[:,[0]]
V_test = test[:,1]

X_test = np.hstack((np.ones((T_test.shape[0],1)),T_test))

V_est_T = (X_test@n).T
Error = np.sum((V_test-V_est_T)**2)/test.shape[0]
print(f"Error in Testing ={Error}")

plt.plot(x,y)
plt.scatter(T_test,V_test, color ='red')
plt.savefig('../figs/Test_GD.png')


