import numpy as np
import matplotlib.pyplot as plt

#import sys
#sys.path.insert(0,'/home/pratik/CoordGeo')

#from line.funcs import *
#from conics.funcs import *

def mu_i(V, u, m, h, f):
    r1 = m.T@V@m
    r2 = m.T@(V@h+u)
    g = h.T@V@h + 2*u.T@h + f
    mu_1 = (-1*r2 + np.sqrt(r2**2 - r1*g))/(r1)
    mu_2 = (-1*r2 - np.sqrt(r2**2 - r1*g))/(r1)

    return mu_1, mu_2


a = 5
c = 5
theta = np.pi/3

B = np.array([[0],[0]])
C = np.array([[a],[0]])
A = c*np.array([[np.cos(theta)],[np.sin(theta)]])

#SIDE LENGTH b

b = np.linalg.norm(A-C)

#CIRCUMCENTER
con1 = (B-C).T
res1 = (B-C).T@(B+C)/2

con2 = (B-A).T
res2 =(B-A).T@(B+A)/2

con = np.vstack((con1,con2))
res = np.vstack((res1,res2))

C = np.linalg.solve(con,res)
print(f"CIRCUMCENTER:{C}")

#PARAMETERS FOR CIRCUMCIRCLE
Area = a*c*np.sin(theta)/2
R = a*b*c/(4*Area)
V = np.array([[1,0],[0,1]])
u = -1*C
f = C.T@C - R**2

#INCENTER
I = (a*A + b*B + c*C)/(a+b+c)
print(f"INCENTER: {I}")

#ANGULAR BISECTORS
m1 = I-A
m2 = I-B
m3 = I-C

#FINDING D
mu_D = mu_i(V,u,m1,A,f)[0]
D = A + mu_D*m1

print(f"D:{D}")

#FINDING E
mu_E = mu_i(V,u,m2,B,f)[0]
E = B + mu_E*m2
print(f"E: {E}")

#FINDING F
mu_F = mu_i(V,u,m3,C,f)[0]
F = C + mu_F*m3
print(f"F: {F}")

cos_ang = (D-E).T@(F-E)/(np.linalg.norm(D-E)*np.linalg.norm(F-E))

cos_2E = 2*cos_ang**2 -1
print(f"cos(2E) : {cos_2E}")
angE = np.arccos(cos_ang)

print(f"ANGLE E:{angE}")
print(f"Error = {np.pi/2 - angE - theta}")






