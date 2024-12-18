import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT= pygame.USEREVENT + 1
BACKGROUND_COLOR_CHNAGE_EVENT= pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
MAGNETA = pygame.Color('magneta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice[-1, 1]], random.choice([-1, 1])
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.bottom >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if boundary_hit:
         pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
         pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHNAGE_EVENT))
    def chnage_color(self):
        self.image.fill(random.choice([YELLOW, MAGNETA, ORANGE, WHITE]))
    def change_background_color():
        global bg_color 
        bg_color = random.choice([BLUE,LIGHTBLUE, DARKBLUE ])
        
    

            
