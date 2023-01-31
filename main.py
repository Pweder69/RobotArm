import time
import math
import simpleio
import analogio
import digitalio
from adafruit_motor import stepper,servo
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

stpPot = analogio.AnalogIn(board.A0)


motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

# QOL implement servoDef example code to make defintions better to change and understand.
rotaServ = servo.Servo(pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50))
armLeft  = servo.Servo(pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50))
armRight = servo.Servo(pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50))


def valMap(xPotentiometer,xRng,yRng):
    if xPotentiometer < 65535/2:
        rVal = simpleio.map_range(xPotentiometer,0,65535/2,-1,-10)
        print("first")
    else:
        rVal = simpleio.map_range(xPotentiometer,65535/2,65535,10,1)
    print(rVal)
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

def direcManager(interval):
    global timeInt
    time = timeInt
    #global because needs to change value
    if time == abs(interval) or time == 10:
        timeInt -= abs(math.floor(interval))
        print("entered loop")
        #better way to controll direction
        if interval < -2:
            motor.onestep(direction=2)
            print("b")
        elif interval > 2:
            print("f")    
            motor.onestep() 
        else: 
            print("stop")
            pass

prevState = 0     
GrabClose = False      
def Grab(buttonVal):
    btnOn = 1
    # BtnOn is a placeHolder for the value witch represnts the button being on 
    # because at the time of writing logic servos and buttons not implemented
    global prevState
    global GrabClose

    if buttonVal == btnOn and buttonVal != prevState:
        prevState = btnOn
        not GrabClose
        if GrabClose == True:
            pass
            #code for servos to open 
        else:
            pass
            #code for servos to close  
    elif buttonVal == 0:
        prevState = 0
     
    
    



while True:
    timeInt +=1
    timeContoller = medianCalc(valMap(stpPot.value,[-1,-10],[10,1]))
    # push the most recent value to runningMedian
    # pop the oldest from the front of runningMedian if there's more than some number of elements there
    # compute the median of runningMedian and store it in a var for this loop
    
    #print(stpPot.value)
    #print(timeInt)
    #print(f"smothedVal:{timeContoller} ")
    #direcManager(timeContoller)
    time.sleep(.05)

