#!/usr/bin/python3

from gpiozero import LightSensor
from time import sleep

ldr = LightSensor(18)


    # Main loop
while True:
    try:
        sleep(0.1)
        print(ldr.value)
    except KeyboardInterrupt:
        sys.exit(0)
    
