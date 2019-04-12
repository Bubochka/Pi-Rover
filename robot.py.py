# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:44:21 2018

@author: Home
"""

import pygame
import RPi.GPIO as GPIO
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Test')

# Assign your RPi pins here
fwdleft = 19
fwdright = 21
revleft = 16
revright = 20

motors = [fwdleft,fwdright,revleft,revright]
for item in motors:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(item, GPIO.OUT)

# Setup for realtime commands. To issue commands for set time use time.sleep().

def forward():
    print("Going forward!")
    GPIO.output(fwdright, True)
    GPIO.output(fwdleft, True)
    
def right():
    print("Going right!")
    GPIO.output(fwdright, True)
    GPIO.output(revleft, True)
	
def left():
    print("Going left!")
    GPIO.output(revright, True)
    GPIO.output(fwdleft, True)
	
def reverse():
    print("Going reverse!")
    GPIO.output(revright, True)
    GPIO.output(revleft, True)

def stop():
    for item in motors:
        GPIO.output(item, False)
        print("stopped")

try:
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        print("Left key pressed")
                                        left()
                                if event.key == pygame.K_RIGHT:
                                        print("Right key pressed")
                                        right()
                                if event.key == pygame.K_UP:
                                        print("Up key pressed")
                                        forward()
                                if event.key == pygame.K_DOWN:
                                        print("Down key pressed")
                                        reverse()
                        
                        elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT:
                                        print("Left key up")
                                        stop()
                                if event.key == pygame.K_RIGHT:
                                        print("Right key up")
                                        stop()
                                if event.key == pygame.K_UP:
                                        print("Up key up")
                                        stop()
                                if event.key == pygame.K_DOWN:
                                        print("Down key up")
                                        stop()
					
except KeyboardInterrupt:
        GPIO.cleanup()