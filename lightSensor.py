#!/usr/bin/python3

import sys
from gpiozero import LightSensor
from time import sleep
from timeit import default_timer as timer

ldr = LightSensor(18)
oldLightState = "off"
lightState = ""

    # Main loop
while True:
    try:
        sleep(0.05)
        #print(ldr.value)
        if ldr.value < 0.5:
            lightState = "off"
        else:
            lightState = "on"
        if oldLightState != lightState:
            #start = timer()
            print(lightState)
            oldLightState = lightState
        else:
            print(lightState)
    except KeyboardInterrupt:
        sys.exit("Operation cancelled by user")
    
