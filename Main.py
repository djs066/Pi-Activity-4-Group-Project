########################################
# Group: Daniel Sauer, 
# Date: 2/19/24
# Assignment: Pi activity 4, Simon Says
########################################
import RPi.GPIO as GPIO
from time import sleep
import pygame

#intialize pygame library
pygame.init()

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
