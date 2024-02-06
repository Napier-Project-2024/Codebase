#!/usr/bin/env python3
import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)
    
while True:
    status = arduino.readline()
    print(status[0])
    
