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
import os

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
    WELCOME_MESSAGE = ""

    #Do not use C:\\directory\\directory2
    #Do not use root directory of the VS code project
    # important for 132 pi project

    #LED = power into LED circuit
    #Switch = input from respective switch

    BUTTONS = [
        Button(switch=20, led=6, sound=os.path.join("sounds", "one.wav"), color="red"),          #Note: anytime file systems are dealt with (folders), import OS
        Button(switch=16, led=13, sound=os.path.join("sounds", "two.wav"), color="blue"),
        Button(switch=12, led=19, sound=os.path.join("sounds", "three.wav"), color="yellow"),
        Button(switch=26, led=21, sound=os.path.join("sounds", "four.wav"), color="green"),
    ]   

    def __init__(self, debug=True):
        self.debug = debug
        self.sequence: list[Button] = []            #Python 3.10+ only?

    def debug_out(self, *args):
        if self.debug:
            print(*args)

    def blink_all_buttons(self):
        leds = []

        for button in Simon.BUTTONS:
            leds.append(button.led)

        GPIO.output(leds, True)                     #Note: technically untested on potato
        sleep(0.5)
        GPIO.output(leds, False)
        sleep(0.5)

        #alternative if above doesn.t work
        # for button in Simon.Buttons:
        #   Button.turn_light_on()
        #   sleep(0.5)
        #   Button.turn_light_off()
        #   sleep(0.5)

    def add_to_sequence(self):
        random_button = choice(Simon.BUTTONS)
        self.sequence.append(random_button)

    def lose(self):
        for _ in range(4):                          #num of times LEDS blink when lose
            self.blink_all_buttons
        GPIO.cleanup()
        exit()

    def playback(self):
        for button in self.sequence:
            button.respond()

    def wait_for_press(self):
        while True:
            for button in Simon.BUTTONS:
                self.debug_out(button.color)
                button.respond()
                return button                       #Kills the while True and tells which button was pressed


    def check_input(self, pressed_button, correct_button):
        if pressed_button.switch != correct_button.switch:
            self.lose()

    def run(self):
        print(self.WELCOME_MESSAGE)

        #game starts with 3 items in the sequence, 2 here 1 from loop
        self.add_to_sequence()
        self.add_to_sequence()

        # use control+c to kill game
        try:
            while True:
                self.add_to_sequence()
                self.playback()
                self.debug_out(*self.sequence)
                
        except KeyboardInterrupt:
            pass