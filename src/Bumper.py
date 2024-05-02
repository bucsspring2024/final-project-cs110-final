import pygame


class Bumper(pygame.sprite.Sprite):
    def __init__(self, x=1, y=1, color="black", width=150, height=10):
        """
        Initialize the bumper objects

        Parameters:
        x (int): The initial x-coordinate of the bumper.
        y (int): The initial y-coordinate of the bumper.
        color (str): The color of the bumper.
        width (int): The width of the bumper.
        height (int): The height of the bumper.
        """
        super().__init__()
        self.starting_xpos = x
        self.starting_ypos = y
        self.width = width
        self.height = height
        self.image = pygame.surface.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bumper_vel = 90

    def move(self, dir_x, dir_y):
        """
        Move the bumper based on the specified directions.

        Parameters:
        dir_x (str): The direction in which to move the bumper horizontally.
        dir_y (str): The direction in which to move the bumper vertically.
        """
        if dir_x == "left":
            self.rect.x -= self.bumper_vel
        if dir_x == "right":
            self.rect.x += self.bumper_vel
        if dir_y == "up":
            self.rect.y -= self.bumper_vel
        if dir_y == "down":
            self.rect.y += self.bumper_vel
        
    def reset(self):
        """
        Reset the bumper position.
        """

        self.rect.x = self.starting_xpos
        self.rect.y = self.starting_ypos