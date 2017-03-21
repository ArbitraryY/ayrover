#!/usr/bin/python
"""@package ayRover
Documentation for this module
"""

import sys
import ConfigParser
#read values from rover.cfg
config = ConfigParser.ConfigParser()
config.read('config/rover.cfg')
sys.path.append(config.get('setup','INSTALL_PATH')+"/ayrover/modules")
print(sys.path)

from OSC import OSCServer
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from Movement import Robot as move
import time
from time import sleep
import atexit

#Instantiate server
oscSrv = OSCServer((config.get('osc_srv','IP'),config.getint('osc_srv','PORT')))

#instantiate movement object
moveRover = move.Robot(left_id=config.getint('motor_params','LEFT_MOTOR_ID'),
                       right_id=config.getint('motor_params','RIGHT_MOTOR_ID'),
                       left_trim=config.getint('motor_params','LEFT_TRIM'),
                       right_trim=config.getint('motor_params','RIGHT_TRIM'))


def move(path,tags,args,source):
    '''
    '''
    #get the second argument in the OSC message with is direction
    mDirection = path.split("/")[2].strip()
    #get the value that's passed with the OSC message
    msgVal     = args[0]
    print path
    print tags
    print args
    print source
    print mDirection
    print '-----------'
    if mDirection == 'forward' and msgVal == 1:
        moveRover.forward(config.getint('motor_params','DEFAULT_SPEED'))
    elif mDirection == 'backward' and msgVal == 1:
        moveRover.backward(config.getint('motor_params','DEFAULT_SPEED'))
    elif mDirection == 'right' and msgVal == 1:
        moveRover.right(config.getint('motor_params','DEFAULT_SPEED'))
    elif mDirection == 'left' and msgVal == 1:
        moveRover.left(config.getint('motor_params','DEFAULT_SPEED'))
    else:
        moveRover.stop()
        
directions = ['forward','backward','right','left']
#Message Handlers and Callback functions
for direction in directions:
    oscSrv.addMsgHandler("/move/"+direction,move)

print "\n listening on port: %s" % config.get('osc_srv','PORT') 

try:
    while True:
        oscSrv.handle_request()

except KeyboardInterrupt:
    print "Quit"
    oscSrv.close()
