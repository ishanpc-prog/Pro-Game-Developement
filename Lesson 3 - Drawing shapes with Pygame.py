import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("Shape drawing session")
running = True
while running:
    screen.fill((30,130,230))
    pygame.draw.rect(screen,(230,223,0),(200,150,200,100),5)
# screen, color, x, y, width, height
# The last object while creating a rectangle is the border width.
# If it is greater than 0 than it gets not filled.
# However if it is zero it is filled
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()