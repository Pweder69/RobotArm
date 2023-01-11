import time
import math
import digitalio
import adafruit_motor
import board
import pwmio
from analogio import AnalogIn, AnalogOut 

coils =[
    digitalio.DigitalInOut(board.D8),  # A1
    digitalio.DigitalInOut(board.D9),  # A2
    digitalio.DigitalInOut(board.D10),  # B1
    digitalio.DigitalInOut(board.D11),  # B2
    ]

pwm = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

def remap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def stepperAdditionMultiplier(xPotentiometer):
    remap(xPotentiometer,0,65535,-10,10)
    return xPotentiometer

while True():
    print(stepperAdditionMultiplier(AnalogIn(board.A0)))

