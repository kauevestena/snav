#!/usr/bin/python

import serial, string, os

portName = '/dev/ttyUSB0'

# this code can run on windows
if os.name == 'nt':
  portName = '\\.\COM4'

ser = serial.Serial(portName, 9600, 8, 'N', 1, timeout=1)

# thx to code-recipes team!
# function extracted from: https://github.com/ActiveState/code/blob/73b09edc1b9850c557a79296655f140ce5e853db/recipes/Python/510399_Byte_Hex_Hex_Byte_String/recipe-510399.py
# (MIT license)
def HexToByte( hexStr ):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    # The list comprehension implementation is fractionally slower in this case    
    #
    #    hexStr = ''.join( hexStr.split(" ") )
    #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
    #                                   for i in range(0, len( hexStr ), 2) ] )
 
    bytes = []

    hexStr = ''.join( hexStr.split(" ") )

    for i in range(0, len(hexStr), 2):
        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

    return ''.join( bytes )

# GLOonly = "B5 62 06 3E 3C 00 00 00 20 07 00 08 10 00 00 00 01 01 01 01 03 00 00 00 01 01 02 04 08 00 00 00 01 01 03 08 10 00 00 00 01 01 04 00 08 00 00 00 01 01 05 00 03 00 00 00 01 01 06 08 0E 00 01 00 01 01 2C 1D"
# ser.write(HexToByte())

# to use GPS,GLONASS and GALILEO
constellations = "B5 62 06 3E 3C 00 00 00 20 07 00 08 10 00 01 00 01 01 01 01 03 00 00 00 01 01 02 04 08 00 01 00 01 01 03 08 10 00 00 00 01 01 04 00 08 00 00 00 01 01 05 00 03 00 00 00 01 01 06 08 0E 00 01 00 01 01 2E 75"
ser.write(HexToByte(constellations))

#automotive mode, 3D only fix and 10deg mask
automotive = "B5 62 06 24 24 00 FF FF 04 02 00 00 00 00 10 27 00 00 0A 00 FA 00 FA 00 64 00 5E 01 00 3C 00 00 00 00 00 00 00 00 00 00 00 00 86 1B"
ser.write(HexToByte(automotive))

# remove GLL msg
noGLL = "B5 62 06 01 08 00 F0 01 00 00 00 00 00 00 00 2A"
ser.write(HexToByte(noGLL))

# remove GSA msg
noGSA = "B5 62 06 01 08 00 F0 02 00 00 00 00 00 00 01 31"
ser.write(HexToByte(noGSA))

# remove GSV msg
noGSV = "B5 62 06 01 08 00 F0 03 00 00 00 00 00 00 02 38"
ser.write(HexToByte(noGSV))

# enable NAV-POSECEF
enPOSECEF = "B5 62 06 01 08 00 01 01 00 00 00 01 00 00 12 B5"
ser.write(HexToByte(enPOSECEF))

# enable GST
enGST = "B5 62 06 01 08 00 F0 07 00 00 00 01 00 00 07 57"
ser.write(HexToByte(enGST))

print "done!"

ser.close()
