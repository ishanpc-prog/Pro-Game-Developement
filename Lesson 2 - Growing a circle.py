import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (0,255,255)
white = (255,255,255)
black = (0,0,0)
screen.fill(blue)
class mycircle():
    def __init__(self,color,pos,radius,width = 0):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.sc = screen
    def draw(self):
        pygame.draw.circle(self.sc,self.color,self.pos,self.radius,self.width)
    def grow(self,x):
        self.radius = self.radius + x
        pygame.draw.circle(self.sc,self.color,self.pos,self.radius,self.width)
position = (250,250)
radius1 = 40
width1 = 2
pygame.draw.circle(screen,red,position,radius1,width1)
pygame.display.update()
greencircle = mycircle(green,position,radius1 + 20)
yellowcircle = mycircle(yellow,position,radius1 + 10)
while(1):
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            greencircle.draw()
            yellowcircle.draw()
            pygame.display.update()
        elif(event.type == pygame.MOUSEBUTTONUP):
            greencircle.grow(20)
            yellowcircle.grow(10)
            pygame.display.update
        elif(event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            whitecircle = mycircle(white,pos,5)
            whitecircle.draw()
            pygame.display.update()