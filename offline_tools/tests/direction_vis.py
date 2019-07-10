import numpy as np
import math
import tf
import matplotlib.pyplot as plt

# from numpy import genfromtxt 
data = np.genfromtxt("/home/kaue/data/orientationfrontal.csv",delimiter=',',skip_header=1,usecols = (1,2,3,4))

euleres=[]
for q in data:
    euler=tf.transformations.euler_from_quaternion(q,'sxyz')
    euler=map(math.degrees,euler)
    euleres.append(euler)

euleres=np.array(euleres)
print(euleres)

maGraph = plt.plot(euleres)
plt.show(maGraph)