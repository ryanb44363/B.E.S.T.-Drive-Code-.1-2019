# VEX EDR Python-Project
import vex
import sys

# ==================================================================
# ||    ______   _____   ______   _        _    __  __       __   ||
# ||   |  ____| |  _  | |  __  | | |____  | |  / /  \ \     / /   ||
# ||   | |      | | | | | |__| | |  __  | | | / /    \ \   / /    ||
# ||   | |____  | |_| | |  __  | | |__| | | |/ /      \ \_/ /     ||
# ||   |____  | |  ___| | |  | | |  __  | | |\ \       \   /      ||
# ||        | | | |     | |  | | | |  | | | | \ \       | |       ||
# ||    ____| | | |     | |  | | | |  | | | |  \ \      | |       ||
# ||   |______| |_|     |_|  |_| |_|  |_| |_|   \_\     |_|       ||
# ||                                                              ||
# ==================================================================
#This is the code for Sparky's drive and movement, operating through ports 2 
#and 5.  This is a work in progress.
#Author(s): Ryan Bellknapp 
#Team: Fernbank L.I.N.K.S. #701

#region config
joystick1 = vex.Joystick()
right         = vex.Motor(2)
left          = vex.Motor(3)
elevator      = vex.Motor(4)
servo1        = vex.Servo(5)
servo2        = vex.Servo(6)
#time          = time
#x             = vex.Motor(2) and vex.Motor(3)
#endregion config

joystick1.set_deadband(15)
 
while True:
    
#DRIVE CODE (FINAL)
    left.run(joystick1.axis2())
    right.run(joystick1.axis3())

#ELEVATOR CODE (FINAL)
    if joystick1.b7up():
        elevator.run(50)
    if joystick1.b7down():
        elevator.run(-50) 
    if joystick1.b7left():
        elevator.off()

#SERVO CODE (FINAL)
    if joystick1.b5up():
        servo1.position(-40)
        servo2.position(20)
    if joystick1.b5down():
        servo1.position(20)
        servo2.position(-40)

#AUTONOMOUS DRIVE (BETA)
#-------------------------------------------------------------------------------
#Measuements: Diameter: 62.8318530718 inches.   Radius: 10 inches.  Full rotation is 125.6637061436 inches.  1/6 of full rotation is 20.9439510231 inches.  
#Two motor turn @ 100% = 1.24140855612 equates to 60 inches in distance.
#Full Robot Turn: One motor motor turn at 60 degrees is equal to 0.21666666666, while opposite motor turn is equal to 0.10833333333 seconds.  
#Directions:  Forward 60 inches, Turn 60 degrees, Forward 79 inches, Turn 90 
#degrees, Drop hook.
#-------------------------------------------------------------------------------
"""
if joystick1.b6up(True):
    #x = left.run(100) and right.run(100)
    #for x in (1.2):
        #x.run for 1.2
    (left.run and right.run) for 1.2
"""

"""     
if joystick1.b6up(): #Autonomous Start Button is bumper five up.
    #DRIVE TO... (START)
    left.run(100)
    right.run(100)
    if(right.run(100) and left.run(100) == True):
        sys.sleep(1.2)
        left.off()
        right.off()        
        #DRIVE TO... (STOP)
""" 
""" #ORIENTATION (START)
    left.run(100)
    right.run(100)
    #sys.wait_for(0.11)
    #ORIENTATION (STOP
    #DROP HOOK (START)
    servo1.position(20)
    servo2.position(-40)
    #DROP HOOK (STOP)
if joystick1.b6up(): #FAILSAFE (FINAL)
    left.off()
    right.off()
    elevator.off()
    """
    
