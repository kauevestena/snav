import numpy as np


a = np.array([[1,1,1],[2,2,2],[3,3,3]])

b = np.array([1,2,3])

# b = np.append(a,np.ones(3),axis=0)

c = np.matmul(a,b)

print(c)


d = [1,2]

d = tuple(d)

print(d)
