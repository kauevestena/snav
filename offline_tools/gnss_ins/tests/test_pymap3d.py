#!/usr/bin/python

# requires pymap3d

# from __future__ import absolute_import
import pymap3d as pm

# print(pm.__file__)
# from pm import geodetic2ecef

# from pymap3d import geodetic2ecef

# import pymap3d

x,y,z = pm.geodetic2ecef(-25.1,-49.5,978.2)

wgs = pm.Ellipsoid()

e,n,u = pm.ecef2enu(x,y,z,-25.0,-49.0,wgs,True)

# print([x,y,z])

print([e,n,u])

# def main():

#     x,y,z = pm.geodetic2ecef(-25.1,-49.5,978.2)

#     # x,y,z = pymap3d.geodetic2ecef(-25.1,-49.5,978.2)


#     print([x,y,z])

# if __name__ == "__main__":
#     main()