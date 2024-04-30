import pygame

class Puck(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.start_xpos = x
        self.start_ypos = y
        self.radius = radius
        self.max_speed = 1
        self.xspeed = 0
        self.yspeed = 0
        self.image = pygame.surface.Surface([self.radius, self.radius])
        self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def move(self):
        self.rect.x += self.xspeed
        self.rect.x += self.yspeed
        
    def reset(self):
        self.rect.x = self.start_xpos
        self.rect.y = self.start_ypos
        self.xspeed = 0
        self.yspeed = 0