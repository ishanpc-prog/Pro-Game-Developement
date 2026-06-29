import pygame

pygame.init()
WIDTH = 700
HEIGHT = 700
pygame.display.set_caption("SPACE INVADERS")

screen = pygame.display.set_mode([WIDTH,HEIGHT])
red_color = (255,0,0)
yellow_color = (0,255,255)
black_color = (0,0,0)
pygame.font.init()
border = pygame.Rect(345,0,10,700)
health_font = pygame.font.SysFont("Times New Roman", 64)
winner_font = pygame.font.SysFont("Times New Roman", 100)
fps = 60
laser_velo = 8 # velo for velocity
max_lasershots = 3
battle_ship_velo = 5
battle_ship_width = 55
battle_ship_height = 40
red_ship_image = pygame.image.load("images/red_battle_ship.png")
red_ship_scale = pygame.transform.scale(red_ship_image,(battle_ship_width,battle_ship_height))
red_ship = pygame.transform.rotate(red_ship_scale,90) # yellow will 270 degrees bcus that reverses 90 degrees 
yellow_ship_image = pygame.image.load("images/yellow_battle_ship.png")
yellow_ship_scale = pygame.transform.scale(yellow_ship_image,(battle_ship_width,battle_ship_height))
yellow_ship = pygame.transform.rotate(yellow_ship_scale,270) #red ship left and yellow ship right
red_ship_health = 20
yellow_ship_health = 20
winner = ""
game_over = False
game_over_font = pygame.font.SysFont("Times New Roman", 64)
simple_font = pygame.font.SysFont("Times New Roman", 40)
r_bullets = []
y_bullets = []
bg = pygame.image.load("images/space_bg_2.png")
backround = pygame.transform.scale(bg,(WIDTH,HEIGHT))
yellow_object = pygame.Rect(20,375,battle_ship_width,battle_ship_height) #Purpose: Storage of Position and Size
red_object = pygame.Rect(680,375,battle_ship_width,battle_ship_height)   #Purpose: Storage of Position and Size

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,black_color,border)
    red_healthbar = health_font.render("Health: " + str(red_ship_health),1,red_color)
    yellow_healthbar = health_font.render("Health: " + str(yellow_ship_health),1,yellow_color)
    screen.blit(red_healthbar,(10,10))
    screen.blit(yellow_healthbar,(600,10))
    screen.blit(red_ship,(red.x,red.y))
    screen.blit(yellow_ship,(yellow.x,yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(screen,red_color,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,yellow_color,bullet)
    pygame.display.update()

#Refer to your birthday animation to render the yellow and red health