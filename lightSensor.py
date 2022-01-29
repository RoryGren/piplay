#!/usr/bin/python3

import sys
from gpiozero import LightSensor
from time import sleep
from timeit import default_timer as timer

ldr = LightSensor(18)
oldLightState = "off"
lightState = ""
flashes = ""
message = ""
start = timer()

MORSE_CODE_DICT = { 'A':'.-',     'B':'-...',
                    'C':'-.-.',   'D':'-..',     'E':'.',
                    'F':'..-.',   'G':'--.',     'H':'....',
                    'I':'..',     'J':'.---',    'K':'-.-',
                    'L':'.-..',   'M':'--',      'N':'-.',
                    'O':'---',    'P':'.--.',    'Q':'--.-',
                    'R':'.-.',    'S':'...',     'T':'-',
                    'U':'..-',    'V':'...-',    'W':'.--',
                    'X':'-..-',   'Y':'-.--',    'Z':'--..',
                    '1':'.----',  '2':'..---',   '3':'...--',
                    '4':'....-',  '5':'.....',   '6':'-....',
                    '7':'--...',  '8':'---..',   '9':'----.',
                    '0':'-----',  ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.',   '-':'-....-',
                    '(':'-.--.',  ')':'-.--.-'}


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
            #print(lightState)
            end = timer()
            duration = end - start
            if lightState == "on":
                if duration > 1.5:
                    flashes += "-"
                else:
                    flashes += "."
            else:
                if duration > 1.5:
                    flashes += "  "
                else:
                    flashes += " "
                
            oldLightState = lightState
            start = timer()
        #else:
            #print(duration)
        
        print(flashes)
    except KeyboardInterrupt:
        sys.exit("Operation cancelled by user")
    
