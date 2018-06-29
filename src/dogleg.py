from pyfirmata import Arduino, util
import RPi.GPIO as GPIO
import time
from i2clibraries import i2c_hmc5883l
from i2clibraries import i2c_adxl345  # acc


hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
hmc5883l.setContinuousMode()
hmc5883l.setDeclination(9,54)
adxl345 = i2c_adxl345.i2c_adxl345(1)



board = Arduino('/dev/ttyUSB0')
pin2 = board.get_pin('d:2:s')
pin3 = board.get_pin('d:3:s')
pin4 = board.get_pin('d:4:s')
pin5 = board.get_pin('d:5:s')
pin6 = board.get_pin('d:6:s')
pin7 = board.get_pin('d:10:s')
pin8 = board.get_pin('d:8:s')
pin9 = board.get_pin('d:9:s')


HLUangleInit=40
HRUangleInit=40
TLUangleInit=140
TRUangleInit=140

HLBangleInit=135
HRBangleInit=135
TLBangleInit=40
TRBangleInit=40


#set GPIO direction (IN / OUT)

def getAcc():
    return adxl345.getAxes()


def distance():
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BOARD)


    #set GPIO Pins
    GPIO_TRIGGER =11
    GPIO_ECHO =13
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    GPIO.cleanup((GPIO_TRIGGER, GPIO_ECHO))

    return distance


def HLU(angle):
    pin2.write(angle-9)

def HLB(angle):
    pin3.write(angle-3)

def HRU(angle):
    pin4.write(180 - angle - 9)

def HRB(angle):
    pin5.write(180 - angle + 8)

def TLU(angle):
    pin6.write(angle+5)

def TLB(angle):
    pin7.write(angle+15)

def TRU(angle):
    pin8.write(180 - angle +5)

def TRB(angle):
    pin9.write(180 - angle - 10)

def initialPose():

    HLU(90)
    HLB(90)
    HRU(90)
    HRB(90)
    TLU(90)
    TLB(90)
    TRU(90)
    TRB(90)
    time.sleep(2)
    HLU(HLUangleInit)
    HRU(HRUangleInit)
    TLU(TLUangleInit)
    TRU(TRUangleInit)
    HLB(HLBangleInit)
    HRB(HRBangleInit)
    TLB(TLBangleInit)
    TRB(TRBangleInit)
 
    
    time.sleep(3)

def initialPoseShort():

    HLU(60)
    HLB(90)
    
    TRU(110)
    TRB(90)
    
    time.sleep(0.1)
    
    HRU(60)
    HRB(90)
    TLU(110)
    TLB(90)

    time.sleep(0.4)

    HLU(HLUangleInit)
    HLB(HLBangleInit)
   
    TRU(TRUangleInit)
    TRB(TRBangleInit)
  
    
    time.sleep(0.1)
    HRU(HRUangleInit)
    HRB(HRBangleInit)
    
    TLU(TLUangleInit)
    TLB(TLBangleInit)
    
    
    time.sleep(0.5)
def motorangle(action): #20
    
#    HLUangle=[0,0, -(20 + angle_left), 0,  0, 0, 0]
#    HLBangle=[0,0, 0, -(20 + angle_left),  0, 0, 0]

#    HRUangle=[0,0, 0, 0, 0, -(20 + angle_right),  0]
#    HRBangle=[0,0, 0, 0, 0, 0,  -(20 + angle_right)]

#    TLUangle=[0,0, 0, 0, 0,  (angle_left + 30),  -(angle_left + 10)]
#    TLBangle=[0,0, 0, 0, 0,  -(angle_left + 50), -(angle_left + 10)]

#    TRUangle=[0,0,   angle_right + 30,  -(angle_right + 10), 0, 0, 0]
#    TRBangle=[0,0, -(angle_right + 50), -(angle_right + 10), 0, 0, 0]



    HLUangle=[0,0, -20, 0,  0, 0, 0]
    HLBangle=[0,0, 20, -20,  0, 0, 0]

    HRUangle=[0,0, 0, 0, 0, -20,  0]
    HRBangle=[0,0, 0, 0, 0, 20,  -20]

    TLUangle=[0,0, 0, 0, 0,  30,  -10]
    TLBangle=[0,0, 0, 0, 0,  -50, -10]

    TRUangle=[0,0, 30,  -10, 0, 0, 0]
    TRBangle=[0,0, -50, -10, 0, 0, 0]




    HLUangle1=[0,0, -20, 0,  0, 0, 0]
    HLBangle1=[0,0, 20, -20,  0, 0, 0]

    HRUangle1=[0,0, 0, 0, 0, -10,  0]
    HRBangle1=[0,0, 0, 0, 0, -10,  -10]

    TLUangle1=[0,0, 0, 0, 0,  15,  -5]
    TLBangle1=[0,0, 0, 0, 0,  -35, -5]

    TRUangle1=[0,0, 15,  -5, 0, 0, 0]
    TRBangle1=[0,0, -35, -5, 0, 0, 0]
    
    
#    HLUangle2=[0,0, -10, 0,  0, 0, 0]
#    HLBangle2=[0,0, 10, -10,  0, 0, 0]

#    HRUangle2=[0,0, 0, 0, 0, -20,  0]
#    HRBangle2=[0,0, 0, 0, 0, -20,  -20]

#    TLUangle2=[0,0, 0, 0, 0,  15,  -10]
#    TLBangle2=[0,0, 0, 0, 0,  -35, -10]

#    TRUangle2=[0,0, 20,  -20, 0, 0, 0]
#    TRBangle2=[0,0, -40, -20, 0, 0, 0]
    
    #right
    HRUangle2=[0,0, -10, 0,  0, 0, 0]
    HRBangle2=[0,0, 10, -10,  0, 0, 0]

    HLUangle2=[0,0, 0, 0, 0, -20,  0]
    HLBangle2=[0,0, 0, 0, 0, -20,  -20]

    TRUangle2=[0,0, 0, 0, 0,  15,  -5]
    TRBangle2=[0,0, 0, 0, 0,  -35, -5]

    TLUangle2=[0,0, 15,  -5, 0, 0, 0]
    TLBangle2=[0,0, -35, -5, 0, 0, 0]

    
    if action == 0:
        
        for m in range(3):

            for i in range(len(HLUangle)):

                HLB(HLBangleInit+HLBangle1[i])
                HLU(HLUangleInit+HLUangle1[i])
                
                HRB(HRBangleInit+HRBangle1[i])
                HRU(HRUangleInit+HRUangle1[i])
                
                TLB(TLBangleInit+TLBangle1[i])
                TLU(TLUangleInit+TLUangle1[i])


                TRB(TRBangleInit+TRBangle1[i])
                TRU(TRUangleInit+TRUangle1[i])
                
                time.sleep(0.07)
                
            for i in range(len(HLUangle)):

                HLB(HLBangleInit+HLBangle2[i])
                HLU(HLUangleInit+HLUangle2[i])
                
                HRB(HRBangleInit+HRBangle2[i])
                HRU(HRUangleInit+HRUangle2[i])
                
                TLB(TLBangleInit+TLBangle2[i])
                TLU(TLUangleInit+TLUangle2[i])


                TRB(TRBangleInit+TRBangle2[i])
                TRU(TRUangleInit+TRUangle2[i])
                
                time.sleep(0.07)
                
            print(getAcc())
            #time.sleep(0.2)
            
    if action == 1:
        for m in range(6):
            for i in range(len(HLUangle)):

                HLB(HLBangleInit+HLBangle1[i])
                HLU(HLUangleInit+HLUangle1[i])

                TLB(TLBangleInit+TLBangle1[i])
                TLU(TLUangleInit+TLUangle1[i])

                HRB(HRBangleInit+HRBangle1[i])
                HRU(HRUangleInit+HRUangle1[i])

                TRB(TRBangleInit+TRBangle1[i])
                TRU(TRUangleInit+TRUangle1[i])
                
                time.sleep(0.07)
            #initialPoseShort()
            print(getAcc())
            #time.sleep(0.1)

    if action == 2:
        for m in range(6):
            for i in range(len(HLUangle)):

                HLB(HLBangleInit+HLBangle2[i])
                HLU(HLUangleInit+HLUangle2[i])

                TLB(TLBangleInit+TLBangle2[i])
                TLU(TLUangleInit+TLUangle2[i])

                HRB(HRBangleInit+HRBangle2[i])
                HRU(HRUangleInit+HRUangle2[i])

                TRB(TRBangleInit+TRBangle2[i])
                TRU(TRUangleInit+TRUangle2[i])
                
                time.sleep(0.07)
                
            print(getAcc())
            #time.sleep(0.1)

def obstacle_distance():
    dist = distance()
    print ("Measured Distance = %.1f cm" % dist)

    return (dist)

def current_direction():

    degree, minutes = i2c_hmc5883l.getHeading()

def isarrived():
    GPIO.setup(16,GPIO.IN)

    try:
        # while (m <= 10):            # this will carry on until you hit CTRL+C
        if GPIO.input(16): # if port 25 == 1
            return (True)
        else:
            return (False)
        time.sleep(0.1)         # wait 0.1 seconds

    finally:                   # this block will run no matter how the try block exits
        GPIO.cleanup(16)         # clean up after yourself


#initialPose()
#while(1):
    
#    #time.sleep(10)
#    motorangle(0)

#    dist = obstacle_distance()
#    #time.sleep(5)

