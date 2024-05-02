import pygame

class Puck(pygame.sprite.Sprite):
    """
    A class representing a ball in a game.

    Attributes:
    starting_xpos (int): The initial x-coordinate of the ball.
    starting_ypos (int): The initial y-coordinate of the ball.
    radius (int): The radius of the ball.
    max_vel (int): The maximum velocity of the ball.
    x_vel (int): The current velocity of the ball in the x-direction.
    y_vel (int): The current velocity of the ball in the y-direction.

    Methods:
    __init__(self, x, y, radius): Initializes a new Ball instance with the specified parameters.
    move(self): Updates the position of the ball based on its current velocity.
    reset(self): Resets the position and velocity of the ball to its initial state.
    """

    def __init__(self, x, y, radius):
        """
        Initializes a new Ball object.

        Parameters:
        x (int): The initial x-coordinate of the ball.
        y (int): The initial y-coordinate of the ball.
        radius (int): The radius of the ball.
        """

        super().__init__()
        self.starting_xpos = x
        self.starting_ypos = y
        self.radius = radius
        self.max_vel = 1
        self.x_vel = 0
        self.y_vel = 0
        # Surface -> circle
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Create a transparent surface
        pygame.draw.circle(self.image, (139, 69, 19), (radius, radius), radius)  # Draw a filled circle on the surface
        self.rect = self.image.get_rect(center=(x, y))

    def move(self):
        """
        Updates the position of the ball based on the velocity.
        """
        
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def reset(self):
        """
        Resets ball position and velocity.
        """
        self.rect.x = self.starting_xpos
        self.rect.y = self.starting_ypos
        self.y_vel = 0
        self.x_vel = 0