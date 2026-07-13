import pygame

pygame.init()
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.font.init()

pygame.display.set_caption("Ping Pong")
running = True

while running:
    screen.fill((200,150,255))
    # pygame.draw.rect(screen,rgb,(x-rect, y-rect, width-rect, height-rect))
    pygame.draw.rect(screen,(255,255,255),(50,250,10,40)) # left rectangle
    pygame.draw.rect(screen,(255,255,255),(450,250,10,40)) # right rectangle
    # pygame.draw.circle(screen,rgb,pos,radius,width)
    pygame.draw.circle(screen,(255,0,0),(250,250),20) # le ball    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
pygame.quit()