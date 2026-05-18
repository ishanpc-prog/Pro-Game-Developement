import pygame
from pygame.locals import *
import time

pygame.init()
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH,HEIGHT])
player_x = 200
player_y = 200

keys = [False,False,False,False]
rocket1 = pygame.image.load("images/rocket3.png")
bg = pygame.image.load("images/space.png")

while player_y < 500 or player_x < 500:
    screen.blit(bg,(0,0))
    screen.blit(rocket1,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type()