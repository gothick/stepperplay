#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import traceback
import logging
# pip3 install rpimotorlib
from RpiMotorLib import RpiMotorLib

def main():
    mymotortest = RpiMotorLib.BYJMotor("Barom", "Nema")
    AIN1 = 6
    AIN2 = 13
    BIN1 = 5
    BIN2 = 0
    GpioPins = [AIN1, BIN1, AIN2, BIN2]
    time.sleep(1)
    input("Press <enter> to test")

    # Test One
    wait = 0.001
    steps = 157 # No of step sequences
    ccwise = True
    verbose= False
    steptype = "half"
    initdelay = 1

    for i in range(0,6):
        mymotortest.motor_run(GpioPins ,wait ,steps ,ccwise ,verbose, steptype ,initdelay)
        ccwise = not ccwise


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print("Caught exception")
        logging.error(traceback.format_exc())
    finally:
        GPIO.cleanup()
        exit()
        
