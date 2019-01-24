#!/usr/bin/python

import serial, string, os

portName = '/dev/ttyUSB0'

if os.name == 'nt':
  portName = '\\.\COM4'

ser = serial.Serial(portName, 9600, 8, 'N', 1, timeout=1)

while True:
  # print "----"
  # while output != "":
  output = ser.readline()
  print output
  # output = " "
