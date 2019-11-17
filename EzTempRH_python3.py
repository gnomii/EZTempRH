#!/usr/bin/python

import serial

# on rpi2: /dev/ttyAMA0
# on rpi3: /dev/ttyS0
with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

    ser.write(str.encode("v"))
    s = ser.read(4)
    version = (s[1] << 8) + s[2]
    print('EzTemp&RH build ' + str(version))

    ser.write(str.encode("d"))
    s = ser.read(4)
    temperature = (s[1] << 8) + s[2]
    print('Temperature: ' + str(1.0*temperature/10) + 'C')

    ser.write(str.encode("i"))
    s = ser.read(4)
    humidity = (s[1] << 8) + s[2]
    print('Relative Humidity:    ' + str(1.0*humidity/10) + '%')

    ser.write(str.encode("x"))
    s = ser.read(4)
    external = (s[1] << 8) + s[2]
    print('External:    ' + str(external) + ' / 2048 counts')

    ser.close()
