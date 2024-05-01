import pygame


class Bumper(pygame.sprite.Sprite):
    def __init__(self, x=1, y=1, color="black", width=150, height=10):
        """
        Initialize the paddle objects

        Parameters:
        x (int): The initial x-coordinate of the paddle.
        y (int): The initial y-coordinate of the paddle.
        color (str): The color of the paddle.
        width (int): The width of the paddle.
        height (int): The height of the paddle.
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

    def move(self, dir):
        """
        Move the paddle left or right based on the specified direction.

        Parameters:
        dir (str): The direction in which to move the paddle.
        """
        if dir == "left":
            self.rect.x -= self.bumper_vel
        if dir == "right":
            self.rect.x += self.bumper_vel
        
    def reset(self):
        """
        Reset the paddle position.
        """

        self.rect.x = self.starting_xpos
        self.rect.y = self.starting_ypos