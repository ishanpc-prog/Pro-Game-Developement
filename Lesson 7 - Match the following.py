import pygame 

pygame.init()
WIDTH = 700
HEIGHT = 700
pygame.display.set_caption("Match the following!")
white = (255,255,255)
pygame.font.init()

screen = pygame.display.set_mode([WIDTH,HEIGHT])
screen.fill(white)

subway_surfers_image = pygame.image.load("images/subway_surfers.png")
candy_crush_image = pygame.image.load("images/candy_crush.jpg")
temple_run_image = pygame.image.load("images/temple_run.png")
ludo_image = pygame.image.load("images/ludo.png")

font = pygame.font.SysFont("Times New Roman", 50)
ludo_text = font.render("Ludo",1,(0,0,0))
subway_surfers_text = font.render("Subway Surfers",1,(0,0,0))
candy_crush_text = font.render("Candy Crush",1,(0,0,0))
temple_run_text = font.render("Temple run",1,(0,0,0))

screen.blit(subway_surfers_image,(100,50))
screen.blit(candy_crush_image,(100,200))
screen.blit(temple_run_image,(100,350))
screen.blit(ludo_image,(100,500))
screen.blit(temple_run_text,(350,50))
screen.blit(subway_surfers_text,(350,200))
screen.blit(ludo_text,(350,350))
screen.blit(candy_crush_text,(350,500))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pos_1 = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(255,0,0),(pos_1),40,0)
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            pos_2 = pygame.mouse.get_pos()
            pygame.draw.line(screen,(255,0,0),(pos_1),(pos_2),5)
            pygame.draw.circle(screen,(255,0,0),(pos_2),40,0)
            pygame.display.update()