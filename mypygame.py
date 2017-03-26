# Resources:
# https://www.pygame.org/docs/tut/PygameIntro.html
# http://stackoverflow.com/questions/11603222/allowing-resizing-window-pygame

from __future__ import print_function
import sys, pygame
from pygame.locals import *
from time import sleep

pygame.init()

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode((320, 240), RESIZABLE)
pygame.display.set_caption("Resizing test")

ball = pygame.image.load("intro_ball.gif")
ball_rect = ball.get_rect()

def draw_screen():
    screen.fill((0, 0, 255))
    pygame.draw.rect(
        screen,
        (200, 0, 0),
        (screen.get_width() / 3, screen.get_height() / 3, screen.get_width() / 3, screen.get_height()/ 3))

    pygame.display.update()

draw_screen()

while True:
    print("Loop {}".format(screen.get_width()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(
                (event.w, event.h),
                RESIZABLE)
            draw_screen()

    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > screen.get_width():
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > screen.get_height():
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ball_rect)
    pygame.display.flip()
