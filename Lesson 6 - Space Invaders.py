import pygame

pygame.init()
WIDTH = 700
HEIGHT = 700
pygame.display.set_caption("SPACE INVADERS")

screen = pygame.display.set_mode([WIDTH,HEIGHT])
red = (255,0,0)
yellow = (0,255,255)
black = (0,0,0)
pygame.font.init()
border = pygame.Rect(345,0,10,700)
health_font = pygame.font.SysFont("Times New Roman", 40)
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
yellow_ship = pygame.transform.rotate(yellow_ship_scale,270)