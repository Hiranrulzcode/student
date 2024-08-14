import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")


red=(255,0,0)
green=(0,255,0)
pygame.display.update()

class Rectangle():
    def __init__(self,color,dimensions):
        self.rect_screen=screen
        self.rect_color=color
        self.rect_dimensions=dimensions
    
    def draw(self):
        self.draw_rect=pygame.draw.rect(self.rect_screen, self.rect_color, self.rect_dimensions)


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    red_rect=Rectangle(red, (50,20,100,100))
    green_rect=Rectangle(green, (100,50,150,150))
    red_rect.draw()
    green_rect.draw()
    pygame.display.update()   
    








