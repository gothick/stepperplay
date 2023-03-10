#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import traceback
import logging
# pip3 install rpimotorlib
from RpiMotorLib import RpiMotorLib
from random import randrange

current_pos = 0

def calibrate():
    print("Calibrating")
    steps = 180
    ccwise = True
    steptype = "half"
    initdelay = 1
    wait = 0.001
    verbose = False
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    

def seek_to(pos):
    global current_pos
    print(f"Seeking to {pos} from {current_pos}")
    if (pos == current_pos):
        return
    ccwise = pos < current_pos
    print("Seeking " + "Counterclockwise" if ccwise else "Clockwise")
    steps = abs(pos - current_pos)
    wait = 0.002
    verbose= False
    steptype = "wave"
    initdelay = 1
    mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
    current_pos = pos

def main():
    global mymotortest, GpioPins
    mymotortest = RpiMotorLib.BYJMotor("Barom", "Nema")
    AIN1 = 6
    AIN2 = 13
    BIN1 = 5
    BIN2 = 16
    GpioPins = [AIN1, BIN1, AIN2, BIN2]
    time.sleep(1)
    calibrate()
    for i in range(1, 20):
        seek_to(randrange(0, 157))
        seek_to(0)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Caught exception")
        logging.error(traceback.format_exc())
    finally:
        GPIO.cleanup()
        exit()
        
