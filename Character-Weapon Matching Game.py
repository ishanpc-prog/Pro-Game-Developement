import pygame
import random 

pygame.init()
WIDTH = 1000
HEIGHT = 1000
pygame.display.set_caption("Match the characters to their weapons!")
white = (255,255,255)
pygame.font.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
screen.fill(white)

ninja_image = pygame.image.load("image/ninja.png")
archer_image = pygame.image.load("image/archer.jpg")
wizard_image = pygame.image.load("image/wizard.jpg")
sword_image = pygame.image.load("image/sword.jpg")
bow_image = pygame.image.load("image/bow.png")
magicwand_image = pygame.image.load("magic_wand.jpg")

x_random_1 = random.randint(75,925)
y_random_1 = random.randint(75,925)
x_random_2 = random.randint(75,925)
y_random_2 = random.randint(75,925)
x_random_3 = random.randint(75,925)
y_random_3 = random.randint(75,925)
x_random_4 = random.randint(75,925)
y_random_4 = random.randint(75,925)
x_random_5 = random.randint(75,925)
y_random_5 = random.randint(75,925)
x_random_6 = random.randint(75,925)
y_random_6 = random.randint(75,925)

screen.blit(ninja_image,(x_random_1,y_random_1))
screen.blit(archer_image,(x_random_2,y_random_2))
screen.blit(wizard_image,(x_random_3,y_random_3))
screen.blit(sword_image,(x_random_4,y_random_4))
screen.blit(bow_image,(x_random_5,y_random_5))
screen.blit(magicwand_image,(x_random_6,y_random_6))

while True:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pos_1 = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0),(pos_1),20,0)
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            pos_2 = pygame.mouse.get_pos()
            pygame.draw.line(screen,(0,0,0),(pos_1),(pos_2),5)
            pygame.draw.circle(screen,(0,0,0),(pos_2),20,0)
            pygame.display.update()