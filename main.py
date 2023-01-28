import time
import math
import simpleio
import analogio
import digitalio
from adafruit_motor import stepper
import board
import pwmio
from analogio import AnalogIn, AnalogOut 


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
    return 10 if rVal < .2 and rVal > -.2 else 1 if rVal < yRng/5 and rVal > xRng/5 else rVal 

runningMedian = []
timeInt = 0     
#get rid of globals

def pushToMed(x):
    runningMedian.append(round(x,1))
    if len(runningMedian) == 20:
        runningMedian.pop(0)
    return median(runningMedian)

def median(input):
    sortedArray = input.copy()
    sortedArray.sort()
    length = round(len(sortedArray)/2)
    return sortedArray[length]

def direcManager(time,interval):
    if time == abs(interval):
        time -= abs(interval)
        
        #better way to controll direction
        if timeContoller < -2 and timeContoller != 1:
            motor.onestep(direction=2)
        else:
            motor.onestep()
            
    



while True:
    timeInt +=1
    timeContoller = pushToMed(stepperAdditionMultiplier(pot.value,-10,10))
    # push the most recent value to runningMedian
    # pop the oldest from the front of runningMedian if there's more than some number of elements there
    # compute the median of runningMedian and store it in a var for this loop
    
    print(f"smothedVal:{timeContoller} ")

    time.sleep(.001)

