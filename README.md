# Readme
![photo](https://github.com/Pweder69/RobotArm/blob/master/media/Pasted%20image%2020221009214700.jpeg)

## Description
For our project me and Paul made a container moving robot arm. We were given the choice of many different robot arm types to accomplish a choosen problem. We decided to use a cylindrical arm for its compactibility, simplicity, and 360 degrees of motion. It can move containers up and down to pick them up and put them down. This project utilizes my CAD skills and Paul's code skills.

## Evidence
[Onshape link](https://cvilleschools.onshape.com/documents/76a12370002b4e158dc0ff90/w/c6fda5d17cd50b6392bebcc0/e/56504ddeac2f6499c6a38d30)

## Image 
<img src="https://user-images.githubusercontent.com/112962227/220508171-789f33d6-3d0f-4e3b-8c73-03659eae5918.png" width =600>

![Screenshot 2023-02-20 9 37 31 PM](https://user-images.githubusercontent.com/112962227/220508196-492cb181-0eec-4735-85d5-0e812b9c224c.png)

![unnamed (2)](https://user-images.githubusercontent.com/112962227/224461918-70a85e57-390a-4f13-ba7a-233050a74e4a.jpg) 
  
https://user-images.githubusercontent.com/112962227/221907679-4ad72246-8130-41ef-a95d-29a4b4bbcc13.MOV

https://user-images.githubusercontent.com/112962227/224461800-ce4f22e2-c9de-4834-bafc-8c203dfe9f17.MOV



## Problem to solve 
The human inabillity to move heavy objects like a shipping crate efficiently.

## Smart Goal
By March 10th we will have built a Robot arm that can move a minature shippng container in 3 different axis of motion. When me and Paul move the potentiometers it will go up or down and when we press the button the claw will grab.

## Orginal sketch designs 
![unnamed (1)](https://user-images.githubusercontent.com/112962227/221909583-b4812a45-8270-4bb2-bca7-dd40fa3ed047.jpg)\
This is the earliest concept design for our project, we knew we wanted to do it so we were coming up with ideas of the claw and the moving base. We changed the claw from the top picture for simplicity but the design of the arm remained similar. The base (lower left) we stuck with, cleaning up the design a little, and for the model (bottom right) we had the same system of a screw motor, arm, moving base, but the thing we modified was the holder at the base of the arm to save materials.

![unnamed](https://user-images.githubusercontent.com/112962227/221909623-b5bfc9a7-7264-4542-a661-e37b09235afd.jpg)

For this design sketch its much cleaner and we had a better pictre in our head of what we wanted it to look like. The design pretty much stayed the same as the bottom picture with only slight adjustments. One major change was the Arm shaft design turned into 2 pillars without a grove to save time and materials. 

### Criteria
- Be able to lift a crate
- rotate 360 degrees
- Materials: Acrylic, Arduino, Plastic (3D print), Arduino sheild, thick acrylic, Stepper motor, Servo motors, worm screw, button, potentiometer

### Constraints
- Materials (especially not having metal part to connect screw to stepper)
- Time is a problem especially because of the time it takes to fabricate and also the designing proccess.
- The need for some sturdy parts (metal)

## Problems and solutions 
### Problem #1
-Friction fit joints not being tight enough to hold (especially for our project because its heavy) 
### Solution
- For the solution I asked Mr. H for help and he told me to apply a 0.16mm thicken on each side instead of 0.8 which wasn't working for me the first time
- *side note* the thick acrylic isn't 6.36mm it's more like 5.2mm for something to consider in friction fitting and for design in general.
![Screenshot 2023-03-09 9 26 24 PM](https://user-images.githubusercontent.com/112962227/224207791-4d8dc2de-40ca-42e0-ae4e-e34db5d60903.png)
### Problem #2
- The use of single screws as joints for T-slots so it acts as a rotating joint and creating a less strudy part

https://user-images.githubusercontent.com/112962227/224462111-26fa5078-0c16-4544-8096-05a3ade072be.MOV

*those were very tightly screwed*

### Solution
- I mostly had to reprint parts to include 2 screws to limit movement so I wish I had thought of it earlier. 
### Problem #3 
- This only happened to me once but to make sure to account for nuts and bolts (the nuts were a bigger problem for me)
### solution
- make an assembly and put all the nuts and bolts in their places to see if any parts need to be adjusted. 
![Screenshot 2023-03-09 10 24 24 PM](https://user-images.githubusercontent.com/112962227/224216107-c763dadc-23d7-4424-bb5a-55187e41f26c.png)
![Screenshot 2023-03-09 10 27 29 PM](https://user-images.githubusercontent.com/112962227/224216129-97964931-9295-43eb-828d-bba1562986fb.png)

## Planning
![Screenshot 2023-03-09 9 54 58 PM](https://user-images.githubusercontent.com/112962227/224216448-c4a5e8c4-28d0-42d7-9ec5-61374700cde5.png)
This is our planning document from the beggining of the year. This planning shows how long projects can take and the importance of time management. For the research we completed on time and had little difficulty since we already had a good idea in our heads of what we wanted for our project. For the design I was way off in predicting to be done in January; I finished some time around now (March 5th-7th) just hammering our all the small errors near the end while having the frame and main parts in place by Febuary 10th-15th. For the manufacutring, I misjudged again, and we finished this around march 9th to 10th cutting the deadline close. For the code, we were off again, Paul did a good job of completing the code but finished a little later because of some problems and tangents but finished around March 3rd-6th. The takeaway from this information is to show the importance of planning and to make timely and realistic goals to not fall behind. Another thing is to focus on your goals because sometimes engineering can be easy to push off during the schiool year until the last minute so to stick to goals is to succeed


## wiring diagram 
![Alt text](media/main%20wire%20diagram%20robot%20arm_bb.png)
## Reflection
This project was challenging and fun; it was the perfect difficulty for our class. One thing I learned for CAD was to better fasten and vizualize things in Onshape so that it was easier for the assembly. An example of this is including nuts and bolts (listed above) and to use differeny mates like the revolute mate (next to normal mate) other useful ones are slider, planar, parrallel, etc. Another thing I reflected on this project was the use of time; this project has taught me the importance of making realistic goals to complete a project efficiently and if I could do it again I would take more time setting goals. Additionally, picking out a project by listing all the ideas on a board and creating the pros and cons list really helped me pick out a project and to vizualize the best option to make sure you don't bite off more than you can chew. Lastly, this project has taguht me to be more thourough when checking for bugs before printing or cutting because this happened a few times where I had to reprint because of friction fitting or not accounting for a part. In conclusion, this projecct taught me alot about completing projects and trouble shooting for the future, it utilized my CAD skills and Pauls code skills tand was a very fun project to work on.

***
# Documentation of code 
Every section explains the specific parts of the code and how it functions




## Initializations  

``` python

coils =[

digitalio.DigitalInOut(board.D8), # A1

digitalio.DigitalInOut(board.D9), # A2

digitalio.DigitalInOut(board.D10), # B1

digitalio.DigitalInOut(board.D11), # B2

]

# This for loop loops over the board pins and declares them as outputs.   
for coil in coils:

coil.direction = digitalio.Direction.OUTPUT

  ```
This is a list of all the coils used by the stepper motor

```python
SERVOPINS = {board.D5,board.D6,board.D7}

SERVONAMES ={"rotaServ","armLeft,armRight"}

# Stores the values for board pins and names for the potentiometers

for x in range(2):

#loops over the names and board values and Initializes them
pwm = pwmio.PWMOut(SERVOPINS,duty_cycle=2 ** 15, frequency=50)

SERVONAMES = servo.Servo(pwm)
```
similar to above but also stores names 


## Creating the array
these functions smothed over the values by finding the mean of several values as to avoid outliers.
``` python

runningMedian = []

def medianCalc(x):

runningMedian.append(round(x,1))

if len(runningMedian) == 20: # 20 is the max amount of values in the array

runningMedian.pop(0)

return median(runningMedian)

  ```
The Function adds to an array every time the function is called in the loop. This happens untill the function [len](functions##len) returns the max value of 20 which is when we use the pop function to remove the first value in the array. Removing the first value allows values to flow similar to a conveyor belt.  
``` python
for x in range(1,8):
	medianCalc(x)

[1]
[1,2]
[1,2,3]
[1,2,3,4]
[1,2,3,4,5]
[2,3,4,5,6]
[3,4,5,6,7]
```

Also note that the array "***runningMedian***" is a global variable, as putting inside the function would restrict it to the scope of a single reference or call.
***

## Calculating the median
Function that calculates the median of the array.
```python

def median(input):

sortedArray = input.deepcopy()

sortedArray.sort()
# sorts the list least to greatest
length = round(len(sortedArray)/2)
#rounds the length/2 to get the location of the center value
return sortedArray[length]
#returning the center value 
```
The median is the center value of a sorted list of numbers. In this function we first make a 
[[functions#.deepcopy() |deepcopy()]] of the list sort the list numericaly then calculate the center by rounding half of the length of the list and then return that value.

Step by step
``` 
[1,5,4,0,3] #sort
[0,1,3,4,5] #find center value
5/2 = 2.5   # round and find that value through indexing
list[3]= 3  # the median is 3

```
***
## Controlling the button state
This code takes the input of a button and decides the state of the grabber arm from closed to open.  The reason we can't just take the input from the button is that the output is a constant on or off of the button, and we need to measure the change in that on or off to control what the button does, not the constant state of the button.

``` python 

prevState = 0    
GrabClose = False      

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
    elif  not buttonVal:
        prevState = False
    return "open" if GrabClose == True else "close

```

First, the reason we use global variables is that we can't reset the value of the state of the arm nor the previous state, as they must stay consistent in between runs of the function.  Next the debouncer, it takes the current value and compares it to the last value of the button if they are the same we know that the button was not pressed if the opposite is true we can change the previous state to on and flip the state of the button in this case the variable of "GrabClose".
***
## Managing the direction of the stepper 
The way the stepper changes is effected by the delay the range of the delay is shown below in the graph

![](https://i.imgur.com/2AHTljy.png)
in the code bellow the range is shown as the function creates this graph and uses it to determine the direction represented by the letters (F,S,B)
``` python
def direcManager(interval):
    global lastDirec
    global timeInt
    time = timeInt

   
    #global because needs to change value

    if time > abs(interval) or time == 10:
        timeInt = 0
        #better way to controll direction
        if interval >=-9 and interval <= -1:
            motor.onestep(direction=2)
            lastDirec = "b"
        elif interval <= 9 and interval >= 1:    
            motor.onestep()
            lastDirec = "f"
        else:
            lastDirec = "s"
    return lastDirec
```
when the delay is smaller the the stepper moves faster and the negative and positive range determines the direction
***

## Planing 
overall the planning was very basic and only revolved around the design aspects of the project so no phudocode was written untill the acutal start of implemetation functions such as the smoothing function were only conceptualized right before writing them A lot of ms paint was used to conceptulize things such as line graph seen in [Managing the direction of the stepper](#managing-the-direction-of-the-stepper) overall the concepts werent that complicated and didnt require planning.


## Reflection 
overall the hardest part of this project was fixing bugs and figuring out the librarys used. A good example of bugs was the issue with using functions such as copy instead of deepcopy as in regular python the correct function is deepcopy but in this version you just use the copy function. Another aspect was the fact that some design decitions changed during the project such  as the control surface. In the future i would give myself more times to fix bugs and wireing.

