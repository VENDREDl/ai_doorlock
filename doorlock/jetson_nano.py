# import Jetson.GPIO as GPIO
import serial

def jetson_nano(count, p):
    if count > 50 and p == 0:
        val = '1'

        val = val.encode('utf-8')
        # GPIO.setup(33, GPIO.LOW)
        print("IN")
        count = 0
        p = 1
    elif count > 5 and p == 1:
        val = '1'

        val = val.encode('utf-8')
        # GPIO.setup(33, GPIO.HIGH)
        print("IN")
        count = 0
        p = 0

def arduino():
    ser = serial.Serial('COM3', 9600)

    while True:

        val = input()

        if val == '1':
            val = val.encode('utf-8')
            ser.write(val)
        elif val == '0':
            val = val.encode('utf-8')
            ser.write(val)
