#!/usr/bin/python3

import sys
from gpiozero import LightSensor
from time import sleep
from timeit import default_timer as timer

ldr = LightSensor(18)

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


def decrypt(message):
 
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher


# Main loop
def main():
    lightState = ""
    flashes = ""
    message = ""
    duration = 0

    oldLightState = "off"
    receiving = "true" 
    start = timer()

    while receiving:
        try:
            sleep(0.05)
            if ldr.value < 0.5:
                lightState = "off"
            else:
                lightState = "on"
            if oldLightState != lightState:
                end = timer()
                duration = end - start
                if oldLightState == "on":
                    if duration > 1.5:
                        flashes += "-"
                    else:
                        flashes += "."
                else:
                    if duration > 3:
                        #end of message
                        receiving = "false"
                        break
                    if duration < 1.5:
                        #inter-letter space
                        flashes += " "
                    else:
                        #inter-word space
                        flashes += "  "
                oldLightState = lightState
                start = timer()
            else:
                print(duration)
            
            print(flashes)
        except KeyboardInterrupt:
            sys.exit("Operation cancelled by user")

    print(flashes)
    message = decrypt(flashes)
    print(message)
    sys.exit()
 
# Executes the main function
if __name__ == '__main__':
    main()
