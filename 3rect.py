import pygame

class Shape:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

pygame.init()
screen = pygame.display.set_mode((500, 500))
rect1 = Shape(50, 50, 100, 60, (255, 0, 0))    
rect2 = Shape(200, 50, 80, 120, (0, 255, 0))   
rect3 = Shape(125, 180, 150, 50, (0, 0, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255)) 
    rect1.draw(screen)
    rect2.draw(screen)
    rect3.draw(screen)
    pygame.display.update()
pygame.quit()