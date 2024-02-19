########################################
# Group: Daniel Sauer, 
# Date: 2/19/24
# Assignment: Pi activity 4, Simon Says
########################################

import pineworkslabs.RPi as GPIO
from time import sleep
from random import choice
import pygame                                       #Note: error is raised since pygame isnt included w/repository. should work if downloaded on machine
from pygame.mixer import Sound

#intialize pygame library
pygame.init()

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

class Button:

    def __init__(self, switch:int, led:int, sound:str, color:str):
        self.switch = switch
        self.led = led
        self.sound: Sound = Sound(sound)
        self.color = color
        self.setupGPIO()

    def setupGPIO(self):
        GPIO.setup(self.switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led, GPIO.OUT)

    def turn_light_on(self):
        GPIO.output(self.led, True)

    def turn_light_off(self):
        GPIO.output(self.led, False)

    def is_pressed(self):
        pass

    def respond(self):      #Note: what it does when button/switch is pressed
        pass
    
    def __str__(self):
        return self.color


class Simon:
    pass













####################################################################################
# set the GPIO pin numbers
# the LEDs (from L to R). Red, Blue, Yellow, Green
leds = [6, 13, 19, 21 ]

# the sounds that map to each LED (from L to R)

sounds = [ 
pygame.mixer.Sound("one.wav"),
pygame.mixer.Sound("two.wav"),
pygame.mixer.Sound("three.wav"),
pygame.mixer.Sound("four.wav") 
]

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the output pins
GPIO.setup(leds, GPIO.OUT)
print("Watch the LEDs light with sound!")
for i in range(len(leds)):
    # light the current LED
    GPIO.output(leds[i], True)

    # play its corresponding sound
    sounds[i].play()

    # wait a bit, then turn the LED off
    sleep(1)
    GPIO.output(leds[i], False)
    sleep(0.5)
    
    print("Sionara!")
    GPIO.cleanup()
