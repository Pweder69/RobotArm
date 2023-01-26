import time
import math
import simpleio
import analogio
import digitalio
import adafruit_motor
from adafruit_motor import stepper
import board
import pwmio
from analogio import AnalogIn, AnalogOut 
from ulab import numpy as np


coils =[
    digitalio.DigitalInOut(board.D8),  # A1
    digitalio.DigitalInOut(board.D9),  # A2
    digitalio.DigitalInOut(board.D10),  # B1
    digitalio.DigitalInOut(board.D11),  # B2
    ]
for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

pot = analogio.AnalogIn(board.A0)

pwm = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)


def stepperAdditionMultiplier(xPotentiometer,xRng,yRng):
    rVal = simpleio.map_range(xPotentiometer,0,65535,xRng,yRng)
    return 9.9 if rVal < .2 and rVal > -.2 else 0 if rVal < yRng/5 and rVal > xRng/5 else rVal, 

runningMedian = []

def pushToMed(x):
    runningMedian.append(x)
    if len(runningMedian) == 6:
        runningMedian.pop(0)
    return median(runningMedian)

def median(input):
    sortedArray = input
    sortedArray.sort()
    print(sortedArray)
    length = math.floor(len(sortedArray)/2)
    return sortedArray[length]
     


while True:
    
    # push the most recent value to runningMedian
    # pop the oldest from the front of runningMedian if there's more than some number of elements there
    # compute the median of runningMedian and store it in a var for this loop
    
    print(f"med:{runningMedian},smothedVal:{pushToMed(stepperAdditionMultiplier(pot.value,-10,10))} ")

    time.sleep(.05)
   # motor.onestep()

