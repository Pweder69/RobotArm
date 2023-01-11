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
#motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)


def stepperAdditionMultiplier(xPotentiometer):
    rVal = simpleio.map_range(xPotentiometer,0,65535,-10,10)
    return rVal if rVal != 0.166168 or 0.156403 else rVal
    

while True:
    #print(pot.value)
    print(stepperAdditionMultiplier(pot.value))
    time.sleep(.05)
