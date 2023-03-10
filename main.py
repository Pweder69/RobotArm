import time
import math
import simpleio
import analogio
import digitalio as DIo
from adafruit_motor import stepper,servo
import board
import pwmio
from analogio import AnalogIn, AnalogOut 


coils =[
    DIo.DigitalInOut(board.D8),  # A1
    DIo.DigitalInOut(board.D9),  # A2
    DIo.DigitalInOut(board.D10),  # B1
    DIo.DigitalInOut(board.D11),  # B2
    ]
for coil in coils:
    coil.direction = DIo.Direction.OUTPUT

stpPot = analogio.AnalogIn(board.A0)
servPot = analogio.AnalogIn(board.A1)

motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

# QOL implement servoDef example code to make defintions better to change and understand.
rotaServ = servo.Servo(pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50))
armServ  = servo.Servo(pwmio.PWMOut(board.D6, duty_cycle=2 ** 15, frequency=50))
btn = DIo.DigitalInOut(board.D5)
btn.direction = DIo.Direction.INPUT
btn.pull = DIo.Pull.DOWN


def valMap(xPotentiometer,xRng,yRng):
    

    if xPotentiometer < 65535/2:
        rVal = simpleio.map_range(xPotentiometer,0,65535/2,-1,-10)
    else:
        rVal = simpleio.map_range(xPotentiometer,65535/2,65535,10,1)
    
    return rVal

runningMedian = []
timeInt = 0     

# QOL get rid of globals eventually 
#   hard change need to 

def medianCalc(x):
    runningMedian.append(round(x,1))
    if len(runningMedian) == 20:
        runningMedian.pop(0)
    return median(runningMedian)

def median(input):
    sortedArray = input.copy()
    sortedArray.sort()
    length = round(len(sortedArray)/2)
    return sortedArray[length]

lastDirec = "n"

def direcManager(interval):
    global lastDirec
    global timeInt
    time = timeInt

    #change condition for time to subtract thats were bugg is
    #global because needs to change value
    if time > abs(interval) or time == 10:
        timeInt = 0
        #better way to controll direction
        if interval >=-8.5 and interval <= -1:
            motor.onestep(direction=2)
            lastDirec = "b"
        elif interval <= 8.5 and interval >= 1:    
            motor.onestep() 
            lastDirec = "f"
        else: 
            lastDirec = "s"
    return lastDirec        
    

prevState = 0     
GrabClose = False      
def Grab(buttonVal):
    global prevState
    global GrabClose

    if buttonVal and buttonVal != prevState:
        prevState = True
        GrabClose = not GrabClose
        if GrabClose:
            pass
            #code for servos to open 
        else:
            pass
            #code for servos to close  
    elif  not buttonVal:
        prevState = False
    return "open" if GrabClose == True else "close"
     


while True:
    timeInt +=1
    stprbase = medianCalc(valMap(stpPot.value,[-1,-10],[10,1]))
    
    # push the most recent value to runningMedian
    # pop the oldest from the front of runningMedian if there's more than some number of elements there
    # compute the median of runningMedian and store it in a var for this loop
    
    #print(stpPot.value)
    #print(timeInt)
    print(f"stpr:{stprbase} base: {simpleio.map_range(servPot.value,0,65535,0,180) if simpleio.map_range(servPot.value,0,65535,0,180) not in range(70,90) else 90 } btn: {Grab(btn.value)}")
    #direcManager(timeContoller) e
    time.sleep(.005)

