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
#This is the code for Spark 2019 BEST.
#This is a work in progress.
#Author(s): Ryan Bellknapp 
#Team: Fernbank L.I.N.K.S. #701



#-------------------------------------------------------------------------------
#   Before START, make sure that:
#   (Mechanical first, then programming)
#
#Mechanically:
# - Make sure that cortex is On.
# - Make sure that USB-USB is connected from computer to cortex.
# - All motors are connected to their designated ports from cortex to ports.
#  
#Programming:
# - Make sure that code is correct (double check)!
# - When ready, Download, Build, and then Run Fast.
#
#   Trouble Shooting:
#Joystick:
# - If yellow,light is on, charge batteries.
# - If robot red light is on, pair the joystick and the cortex using the USB-USB 
#   cord.
# - If robot red light is on, VexNet is most likely not plugged in or pairing.
#
#Cortex:
# - Ignore Game Light, it isn't relevant.
# - If Robot Red light is on, mainly solid with one blink, code is not working,
#   go back and reconfigure code.
# - If Robot Red Light is on, solid, turn on the robot or charge the battery.
# - If it is not connecting, try turning the cortex on and off again.
#-------------------------------------------------------------------------------
#Preface to Code:
#   Robot Mesh Studio is a software that uses Python (probably 2.7) and is,
#quite frankly, not very good.  The only reason why we used it this year was
#so that we can properly upload code from one's computer to a cortex, which 
#seemed to be a big problem this year.
#   This Studio simply serves as a bridge between the cortex and one's code on
#their computer.  
#   I would like to thank Ibaad Sayeed for his time and effort in attempting to
#code our robot using Simulink, which unfortunately did not work out this year.
#
#                       Yours Truly,
#                                  Ryan Bellknapp
#-------------------------------------------------------------------------------
#region config
joystick1 = vex.Joystick()
right         = vex.Motor(2)
left          = vex.Motor(3)
elevator      = vex.Motor(4)
servo1        = vex.Servo(5)
servo2        = vex.Servo(6)

#endregion config

while True:
    
    joystick1.set_deadband(15)    
    
#DRIVE CODE (FINAL)
    left.run(joystick1.axis2())
    right.run(joystick1.axis3())
#ELEVATOR CODE (FINAL)
    if joystick1.b7down():
        elevator.run(25)
    if joystick1.b7up():
        elevator.run(-85) 
    if joystick1.b7left():
        elevator.off()

#SERVO CODE (FINAL)
    if joystick1.b5down():
        servo1.position(-40)
        servo2.position(20)
    if joystick1.b5up():
        servo1.position(20)
        servo2.position(-40)

#AUTONOMOUS DRIVE (BETA)
#-------------------------------------------------------------------------------
#Measurements: Diameter: 62.8318530718 inches.   Radius: 10 inches.  Full rotation is 125.6637061436 inches.  1/6 of full rotation is 20.9439510231 inches.  
#Two motor turn @ 100% = 1.24140855612 equates to 60 inches in distance.
#Full Robot Turn: One motor motor turn at 60 degrees is equal to 0.21666666666, while opposite motor turn is equal to 0.10833333333 seconds.  
#Directions:  Forward 60 inches, Turn 60 degrees, Forward 79 inches, Turn 90 
#degrees, Drop hook.
#-------------------------------------------------------------------------------

    if joystick1.b8right():
        #green blue Straight
        
        #HOOK UP
        servo1.position(20)
        servo2.position(-40)
        sys.sleep(1)
        #END HOOK PERIOD
        
        #DRIVE PERIOD START 
        right.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        left.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        #left.run(10) #OREINTATION START
        #sys.sleep(.20)
        #right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
    
    
        
        right.run(-90) #225 TURN CLOCKWISE
        left.run(90) 
        sys.sleep(1.5) 
        left.off 
        right.off #END TURN
        
        left.run(-50) #FINAL DRIVE START
        right.run(-30)
        #sys.sleep(3.9)
        sys.sleep(1.25) #FINAL DRIVE END
        left.off #MOTOR OFF
        right.off #MOTOR OFF

        servo1.position(-40) #DROP  HOOK START 
        servo2.position(20)
        sys.sleep(1) #DROP HOOK END 
        right.off
        left.off 
        
        pass #END ALL

    if joystick1.b6up():
        #red yellow Straight (1)
        
        #HOOK UP
        servo1.position(20)
        servo2.position(-40)
        sys.sleep(1)
        #END HOOK PERIOD
        
        #DRIVE PERIOD START 
        right.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        left.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        #left.run(10) #OREINTATION START
        #sys.sleep(.20)
        #right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
    
    
        
        right.run(90) #225 TURN CLOCKWISE
        left.run(-90) 
        sys.sleep(1.5) 
        left.off 
        right.off #END TURN
        
        left.run(-50) #FINAL DRIVE START
        right.run(-30)
        #sys.sleep(3.9)
        sys.sleep(1.25) #FINAL DRIVE END
        left.off #MOTOR OFF
        right.off #MOTOR OFF

        servo1.position(-40) #DROP  HOOK START 
        servo2.position(20)
        sys.sleep(1) #DROP HOOK END 
        right.off
        left.off 
        
        pass #END ALL
    
    if joystick1.b6down():
        #red yellow Straight (2)
        
        #HOOK UP
        servo1.position(20)
        servo2.position(-40)
        sys.sleep(1)
        #END HOOK PERIOD
        
        #DRIVE PERIOD START 
        right.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        left.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        #left.run(10) #OREINTATION START
        #sys.sleep(.20)
        #right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
    
    
        
        right.run(90) #225 TURN CLOCKWISE
        left.run(-90) 
        sys.sleep(1.5) 
        left.off 
        right.off #END TURN
        
        left.run(-50) #FINAL DRIVE START
        right.run(-40)
        #sys.sleep(3.9)
        sys.sleep(1.25) #FINAL DRIVE END
        left.off #MOTOR OFF
        right.off #MOTOR OFF

        servo1.position(-40) #DROP  HOOK START 
        servo2.position(20)
        sys.sleep(1) #DROP HOOK END 
        right.off
        left.off 
        
    if joystick1.b8left():
        #red yellow Straight
        #HOOK UP
        servo1.position(20)
        servo2.position(-40)
        sys.sleep(1)
        #END HOOK PERIOD
        
        #DRIVE PERIOD START 
        right.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        left.run(10) #ORIENTATION START
        sys.sleep(.20)
        right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
        
        #left.run(10) #OREINTATION START
        #sys.sleep(.20)
        #right.off #ORIENTATION END
        
        left.run(100) #DRIVE BOTH MOTORS START
        right.run(100)
        #sys.sleep(3.9)
        sys.sleep(1.3)
        right.off
        left.off #END DRIVE BOTH MOTORS
    
    
        
        right.run(90) #225 TURN CLOCKWISE
        left.run(-90) 
        sys.sleep(1.5) 
        left.off 
        right.off #END TURN
        
        left.run(-50) #FINAL DRIVE START
        right.run(-50)
        #sys.sleep(3.9)
        sys.sleep(1.25) #FINAL DRIVE END
        left.off #MOTOR OFF
        right.off #MOTOR OFF

        servo1.position(-40) #DROP  HOOK START 
        servo2.position(20)
        sys.sleep(1) #DROP HOOK END 
        right.off
        left.off 
        

#Place servo drop statement


#End of Original

#Version Two, Untested Code:

    """
    #Fun - Sparky Salsa - 
    if joystick1.b8down():
        left.run(50)
        right.run(-50)
        servo1.position(-40)
        servo2.position(20)
        sys.sleep(3)
        left.off
        right.off
        
        left.run(-50)
        right.run(50)
        servo1.position(20)
        servo2.position(-40)
        sys.sleep(3)
        left.off
        right.off
        
        left.run(75)
        servo1.position(-40)
        servo2.position(20)
        sys.sleep(1.625)
        servo1.position(20)
        servo2.position(-40)
        left.off
        
        right.run(75)
        servo1.position(-40)
        servo2.position(20)
        sys.sleep(1.625)
        servo1.position(20)
        servo2.position(-40)
        right.off
        
        right.off
        left.off
        pass
        
"""
# THE GRAVEYARD

"""    
    
    if joystick1.b8up():
        left.run_time(100, 2, false)
        right.run_time(100, 2, false)
        quit()
    
    print(infared)
        if infared()
    servo1.position(50)
    servo2.position(50)
"""    


"""
if joystick1.b8left():
    x = left
    left.run(100)
    right.run(100)
         
            left.off()
            right.off()
"""
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

#END AND LOOP INFINITELY 
