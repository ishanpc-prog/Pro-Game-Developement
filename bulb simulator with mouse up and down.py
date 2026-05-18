import pygame
import time
pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("ON-switch and OFF-switch bulb simulator with mouse down and mouse up events")
i1 = pygame.image.load("images/light_bulb_off.png")
image1 = pygame.transform.scale(i1,(WIDTH,HEIGHT))
while True:
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            i2 = pygame.image.load("images/light_bulb_on.png")
            image2 = pygame.transform.scale(i2,(WIDTH,HEIGHT))
            screen.blit(image2,(0,0))
            pygame.display.update()
        elif(event.type == pygame.MOUSEBUTTONUP):
            screen.blit(image1,(0,0))
            pygame.display.update()