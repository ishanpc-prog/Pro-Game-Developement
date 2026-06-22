import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

w1 = pygame.image.load("images/standing_homme.jpg")
w2 = pygame.image.load("images/walking_homme.png")

walk1 = pygame.transform.scale(w1,(800,600))
walk2 = pygame.transform.scale(w2,(800,600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif(event.type == pygame.MOUSEBUTTONUP):
            screen.fill((255,255,255))
            screen.blit(walk1,(0,0))
            pygame.display.update()
        elif(event.type == pygame.MOUSEBUTTONDOWN):
            screen.fill((255,255,255))
            screen.blit(walk2,(0,0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()