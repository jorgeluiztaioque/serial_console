#!/usr/bin/env python3

import serial
import time

with serial.Serial(port='/dev/tty/USB)', baudrate=9600, stopbits=1, bytssize=0, timeout=0)as console:
    if console.isOpen():
        print ("Console port is open")
        console.write(b'\n')
        time.sleep(1)
        console.write(b'enable\n')
        time.sleep(1)
        console.write(b'terminal length 0\n')
        time.sleep(1)
        console.write(b'show version\n')
        time.sleep(3)
        bytes_to_be_read = console.isWaiting()
        output = console.read(bytes_to_be_read)
        print (output.decode())
    else:
        print ("Error to open console connection")
