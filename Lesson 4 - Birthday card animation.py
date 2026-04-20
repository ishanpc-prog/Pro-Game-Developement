import pygame
import time

pygame.init()
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Birthday card animation")
i1 = pygame.image.load("cake.jpg")
image1 = pygame.transform.scale(i1,(WIDTH,HEIGHT))
while True:
    font = pygame.font.SysFont("Times New Roman", 72)
    text1 = font.render("Happy", True, (150,235,235))
    text2 = font.render("Birthday", True, (150,235,235))
    screen.fill((120,120,120))
    screen.blit(image1,(0,0))
    screen.blit(text1,(250,250))
    screen.blit(text2,(270,250))
    pygame.display.update()
    time.sleep(3)