import pygame

class Mallet(pygame.sprite.Sprite):
    def __init__(self, x, y, color, height, width, speed):
        super().__init__()
        self.start_xpos = x
        self.start_ypos = y
        self.height = height
        self.width = width
        self.image = pygame.surface.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mallet_speed = speed
        
    def move(self, dir):
        if dir == "up":
            self.rect.y += self.mallet_speed
        if dir == "down":
            self.rect.y -= self.mallet_speed
        if dir == "left":
            self.rect.x -= self.mallet_speed
        if dir == "right":
            self.rect.x += self.mallet_speed
            
    def reset(self):
        self.rect.x = self.start_xpos
        self.rect.y = self.start_ypos
        