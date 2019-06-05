import numpy
from numpy import genfromtxt
import matplotlib.pyplot as plt

from scipy import stats

angVelPath  = "/home/kauevestena/data/angular_velocity.csv"
accPath     = "/home/kauevestena/data/linear_acceleration.csv"
oriPath     = "/home/kauevestena/data/orientation.csv"

angVelData = numpy.genfromtxt(angVelPath,delimiter=',',skip_header=1)[:,1:]
accData    = numpy.genfromtxt(accPath,delimiter=',',skip_header=1)[:,1:]
oriData    = numpy.genfromtxt(oriPath,delimiter=',',skip_header=1)[:,1:]

angVelStd   = numpy.std(angVelData,0)
accStd      = numpy.std(accData,0)
# oriStd      = numpy.std(oriData,0)

print(angVelStd)
print(accStd)
# print(oriStd)

#standart error
angVelSem   = stats.sem(angVelData,0)
accSem      = stats.sem(accData,0)
oriStd      = numpy.std(oriData,0)

print(angVelSem)
print(accSem)

print("        self.imu_msg.orientation_covariance[0] = 0.5")
print("        self.imu_msg.orientation_covariance[4] = 0.5")  
print("        self.imu_msg.orientation_covariance[8] = 1.0")
print("        self.imu_msg.angular_velocity_covariance[0] = "    + str(angVelStd[0]) )
print("        self.imu_msg.angular_velocity_covariance[4] = "    + str(angVelStd[1]) )
print("        self.imu_msg.angular_velocity_covariance[8] = "    + str(angVelStd[2]) )
print("        self.imu_msg.linear_acceleration_covariance[0] = " + str(accStd[0]) )
print("        self.imu_msg.linear_acceleration_covariance[4] = " + str(accStd[1]) )
print("        self.imu_msg.linear_acceleration_covariance[8] = " + str(accStd[2]) )

h1 = plt.hist(angVelData,20)
plt.show(h1)

h2 = plt.hist(accData,20)
plt.show(h2)

