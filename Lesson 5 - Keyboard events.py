import pygame
from pygame.locals import *
import time

pygame.init()
WIDTH = 700
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH,HEIGHT])
player_x = 200
player_y = 200

keys = [False,False,False,False]
rocket1 = pygame.image.load("images/rocket3.png")
r1 = pygame.transform.scale(rocket1,(200,150))
bg = pygame.image.load("images/space.png")

while player_y < 490:
    screen.blit(bg,(0,0))
    screen.blit(r1,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] == True
            elif event.key == K_DOWN:
                keys[1] == True
            elif event.key == K_LEFT:
                keys[2] == True
            elif event.key == K_RIGHT:
                keys[3] == True
        elif event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] == False
            elif event.key == K_DOWN:
                keys[1] == False
            elif event.key == K_LEFT:
                keys[2] == False
            elif event.key == K_RIGHT:
                keys[3] == False
    if keys[0]:
        if player_y > 0:
            player_y = player_y - 5
    elif keys[1]:
        if player_y < 490:
            player_y = player_y + 5
    elif keys[2]:
        if player_x > 0:
            player_x = player_x - 5
    elif keys[3]:
        if player_x < 490:
            player_x = player_x + 5
    time.sleep(0.05)
print("Game over!")