import numpy as np
import pandas as pd

# Read the data
df = pd.read_csv('data.csv').T

col_0 = df.iloc[0].values
col_0 = col_0.reshape(-1,1)

col_1 = df.iloc[1].values

#Readings = np.array([0,1,2,3])
#print(Readings)
#Temp = np.array([10,20,30,40])

Readings = np.hstack((np.ones(col_0.shape),col_0))

c, m = np.linalg.lstsq(Readings,col_1,rcond = None)[0]

print(f'{c}, {m}')
