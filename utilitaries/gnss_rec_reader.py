#!/usr/bin/python

import serial, string

output = " "
ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1, timeout=1)
while True:
  print "----"
  while output != "":
    output = ser.readline()
    print output
  output = " "
