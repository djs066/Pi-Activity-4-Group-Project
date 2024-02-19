########################################
# Group 1: Daniel Sauer, 
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
        result = GPIO.input(self.switch)
        if result == True:
            return True
        else:
            return False

    def respond(self):                              #Note: what it does when button/switch is pressed
        self.turn_light_on()
        self.sound.play()
        sleep(1)
        self.turn_light_off()
        sleep(0.25)

    
    def __str__(self):
        return self.color


class Simon:
    pass