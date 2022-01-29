#!/usr/bin/python3

import sys
from gpiozero import LightSensor
from time import sleep
from timeit import default_timer as timer

ldr = LightSensor(18)
oldLightState = "off"
lightState = ""
start = timer()
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
            end = timer()
            print(end - start)
            print(lightState)
            oldLightState = lightState
            start = timer()
        else:
            print(lightState)
    except KeyboardInterrupt:
        sys.exit("Operation cancelled by user")
    
