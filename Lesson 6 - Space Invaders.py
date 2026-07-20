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
winner = ""
game_over = False
game_over_font = pygame.font.SysFont("Times New Roman", 64)
simple_font = pygame.font.SysFont("Times New Roman", 40)
bg = pygame.image.load("images/space_bg_2.png")
backround = pygame.transform.scale(bg,(WIDTH,HEIGHT))
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

def draw_window(red,yellow,red_bullets,yellow_bullets,red_ship_health,yellow_ship_health):
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

def red_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - laser_velo > 0:
        red.x = red.x - laser_velo
    elif key_pressed[pygame.K_RIGHT] and red.width + red.x + laser_velo < border.x:
        red.x = red.x + laser_velo
    elif key_pressed[pygame.K_UP] and red.y - laser_velo > 0:
        red.y = red.y - laser_velo
    elif key_pressed[pygame.K_DOWN] and red.height + red.y + laser_velo < 685:
        red.y = red.y - laser_velo

def yellow_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - laser_velo > border.x + border.width:
        yellow.x = yellow.x - laser_velo
    elif key_pressed[pygame.K_d] and yellow.width + yellow.x + laser_velo < 685:
        yellow.x = yellow.x + laser_velo
    elif key_pressed[pygame.K_w] and yellow.y - laser_velo > 0:
        yellow.y = yellow.y - laser_velo
    elif key_pressed[pygame.K_s] and yellow.height + yellow.y + laser_velo < 685:
        yellow.y = yellow.y + laser_velo

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x = bullet.x - laser_velo
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x = bullet.x + laser_velo
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            red_bullets.remove(bullet)
        elif bullet.x > 700:
            red_bullets.remove(bullet)     

def main():
    red = pygame.Rect(680,375,battle_ship_width,battle_ship_height)
    yellow = pygame.Rect(20,375,battle_ship_width,battle_ship_height)
    red_bullets = []
    yellow_bullets = []
    red_ship_health = 20
    yellow_ship_health = 20
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and len(yellow_bullets) < max_lasershots:
                    bullet = pygame.Rect(yellow.x + yellow.width ,  yellow.y + yellow.height // 2-2,10,5)
                    yellow_bullets.append(bullet)
                elif event.key == pygame.K_m and len(red_bullets) < max_lasershots:
                    bullet = pygame.Rect(red.x , yellow.y + yellow.height // 2-2,10,5)
                    red_bullets.append(bullet)
            elif event.type == yellow_hit:
                yellow_ship_health = yellow_ship_health - 1
            elif event.type == red_hit:
                red_ship_health = red_ship_health - 1
        winner_text = ""
        if yellow_ship_health <= 0:
            winner_text = "The red ship has won this match!"
        elif red_ship_health <= 0:
            winner_text = "The yellow ship has won this match"
        elif winner_text != "":
            victory(winner_text) # defined Name is victory