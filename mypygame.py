# Taken from https://www.pygame.org/docs/tut/PygameIntro.html

from __future__ import print_function
import sys, pygame
#from pygame.locals import *
from time import sleep

pygame.init()

size = width, height = 640, 480
black = 0, 0, 0 #idea: make nice background

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

ball1 = pygame.image.load("tennis.png")
ballrect1 = ball1.get_rect()
speed1 = [2, 2]

ball2 = pygame.image.load("ball2.png")
ballrect2 = ball2.get_rect(center=(width/2, height/2))
speed2 = [-2, -2]

mouse_pos = None

def handle_resize_event(event):
    print("resized!")
    global width, height, size, screen
    width = event.w
    height = event.h
    size = width, height
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

def bounce_wall(ballrect, speed):
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    return ballrect

def bounce_balls(ballrect1, ballrect2, speed1, speed2):
    if ballrect1.colliderect(ballrect2):
        if ballrect1.left < ballrect2.left or ballrect2.right > ballrect2.right:
            speed1[0] = -speed1[0]
            speed2[0] = -speed2[0]
        if ballrect1.top < ballrect2.top or ballrect1.bottom > ballrect2.bottom:
            speed1[1] = -speed1[1]
            speed2[1] = -speed2[1]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.VIDEORESIZE: handle_resize_event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN: mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP: mouse_pos = None

    if mouse_pos and ballrect2.collidepoint(mouse_pos):
        speed2 = [0, 0]

    bounce_balls(ballrect1, ballrect2, speed1, speed2)
    ballrect1 = bounce_wall(ballrect1, speed1)
    ballrect2 = bounce_wall(ballrect2, speed2)            

    screen.fill(black)
    screen.blit(ball1, ballrect1)
    screen.blit(ball2, ballrect2)
    pygame.display.flip()
    sleep(0.01)
