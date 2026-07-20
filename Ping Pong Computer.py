import pygame

pygame.init()
WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.font.init()

pygame.display.set_caption("Ping Pong")
running = True
moving_distance = 20
left_health_score = 20
right_health_score = 20

while running:
    screen.fill((200,150,255))
    font = pygame.font.SysFont("Times New Roman", 20)
    l_healthbar = font.render("Health: " + str(left_health_score), True, (0,0,0))
    r_healthbar = font.render("Health: " + str(right_health_score), True, (0,0,0))
    screen.blit(l_healthbar,(15,20))
    screen.blit(r_healthbar,(400,20))
    pygame.draw.rect(screen,(0,0,0),(245,0,10,500)) #border
    # pygame.draw.rect(screen,rgb,(x-rect, y-rect, width-rect, height-rect))
    pygame.draw.rect(screen,(255,255,255),(50,250,20,80)) # left rectangle
    pygame.draw.rect(screen,(255,255,255),(450,250,20,80)) # right rectangle
    # pygame.draw.circle(screen,rgb,pos,radius,width)
    pygame.draw.circle(screen,(255,0,0),(250,250),20) # le ball   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
pygame.quit()

# make padels go up and down by command