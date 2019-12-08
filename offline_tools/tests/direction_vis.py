import numpy as np
import math
import tf
import matplotlib.pyplot as plt

# from numpy import genfromtxt 
data = np.genfromtxt("/home/kaue/data/orientationfrontal.csv",delimiter=',',skip_header=1,usecols = (1,2,3,4))

timedata = np.genfromtxt("/home/kaue/data/orientationfrontal.csv",delimiter=',',skip_header=1,usecols=(0))

#1560451657991781104
#1560451000000000000


timedata -= 1560451418439008471
timedata *= 1e-9

euleres=[]
for q in data:
    euler=tf.transformations.euler_from_quaternion(q,'sxyz')
    euler=map(math.degrees,euler)
    euleres.append(euler)

euleres=np.array(euleres)

# manipulating azimuth
azimuths = euleres[:,2]

azimuths += 180
max_idx = np.argmax(azimuths)
azimuths[max_idx+1:len(azimuths)] += 360
azimuths -= 82 

print(euleres)
print(timedata)



# # # # # pyplot stuff

plt.close('all')
# plt.plot(euleres)
plt.plot(timedata,euleres[:,0],"-r",label="ROLL")
plt.plot(timedata,euleres[:,1],"-b",label="PITCH")
plt.plot(timedata,euleres[:,2],"-g",label="AZIMUTH")
plt.title('ORIENTATION')
plt.xlabel('Time (s)')
plt.ylabel('Angle (deg.)')
plt.legend()
plt.savefig('directions')
# plt.show()


plt.close('all')
# plt.plot(euleres)
plt.plot(timedata,euleres[:,0],"-r",label="ROLL")
plt.plot(timedata,euleres[:,1],"-b",label="PITCH")
plt.plot(timedata,euleres[:,2],"-g",label="AZIMUTE")
plt.title('ORIENTACAO')
plt.xlabel('Tempo (s)')
plt.ylabel('Angulo (deg.)')
plt.legend()
plt.savefig('directions_ptbr')
# plt.show()


plt.close('all')
# plt.plot(euleres)
plt.plot(timedata,data[:,0],label="x")
plt.plot(timedata,data[:,1],label="y")
plt.plot(timedata,data[:,2],label="z")
plt.plot(timedata,data[:,3],label="w")
plt.title('ORIENTACAO')
plt.xlabel('Tempo (s)')
plt.ylabel('valor')
plt.legend()
plt.savefig('directions_quaternion')