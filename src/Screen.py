import pygame

class Screen:
    """
    A class representing different screens in a game.

    Attributes:
    window_width (int): The width of the game window.
    window_height (int): The height of the game window.
    screen (pygame.Surface): The main surface for rendering the game.
    white (tuple): RGB values representing the white color.

    Methods:
    __init__(self): Initializes a new Screens instance and sets up the game window.
    startscreen(self): Renders the start screen with game instructions.
    gamescreen(self): Renders the main game screen with a dividing line.
    endscreen(self, winner="GREEN", green_score=0, purple_score=0): Renders the end screen with the winner and scores.
    """
    def __init__(self):
        """
        Initializes a new Screens instance and sets up the game window.
        """
        pygame.init()
        self.window_width = 500
        self.window_height = 900
        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.white = (255, 255, 255)  # Set background color to white
        
    def startscreen(self):
        """
        Renders the start screen with game instructions.
        """
        self.screen.fill(self.white)
        font = pygame.font.Font(None, 100)
        text = font.render("Bumpers", True, "black")
        intro_text_rect = text.get_rect()
        half_text_width = intro_text_rect.width // 2
        half_text_height = intro_text_rect.height // 2
        intro_text_x_pos = (self.window_width // 2) - half_text_width
        intro_text_y_pos = (self.window_height // 4) - half_text_height
        intro_text_rect_center = (intro_text_x_pos, intro_text_y_pos)
        self.screen.blit(text, intro_text_rect_center)
        
        space_bw_text = 30
        font = pygame.font.Font(None, 30)
        text = font.render("Instructions:", True, "white")
        instru_text_x_pos = 0
        instru_text_y_pos = self.window_height - (self.window_height/3)
        self.screen.blit(text, (instru_text_x_pos, instru_text_y_pos))
        text = font.render("Team Purple: use the arrow keys to move your bumper left, right, up, and down", True, "white")
        instrupurple_text_x_pos = 0
        instrupurple_text_y_pos = instru_text_y_pos + space_bw_text
        self.screen.blit(text, (instrupurple_text_x_pos, instrupurple_text_y_pos))
        text = font.render("Team Green: use the a, d, s, and w keys to move your bumper left, right, up, and down", True, "white")
        instrugreen_text_x_pos = 0
        instrugreen_text_y_pos = instrupurple_text_y_pos + space_bw_text
        self.screen.blit(text, (instrugreen_text_x_pos, instrugreen_text_y_pos))
        text = font.render("Try to get the puck past the opposing teams bumper", True, "white")
        instrugoal_text_x_pos = 0
        instrugoal_text_y_pos = instrugreen_text_y_pos + space_bw_text
        self.screen.blit(text, (instrugoal_text_x_pos, instrugoal_text_y_pos))
        text = font.render("First team to 3 points wins!", True, "white")
        instruwin_text_x_pos = 0
        instruwin_text_y_pos = instrugoal_text_y_pos + space_bw_text
        self.screen.blit(text, (instruwin_text_x_pos, instruwin_text_y_pos))
        
        pygame.display.flip()
        
    def gamescreen(self):
        """
        Creates a dividing line on the main game screen.
        """
        self.screen.fill(self.white)
        pygame.draw.line(self.screen, "black", (0, self.window_height/2), (self.window_width, self.window_height/2), 2)
        
        pygame.display.flip()
        
    def endscreen(self, winner="PURPLE", green_score=0, purple_score=0):
        """
        Renders the end screen with the winner and scores.

        Parameters:
        - winner (str): The winning team, default is "PURPLE".
        - green_score (int): The score of the green team.
        - purple_score (int): The score of the purple team.
        """
        self.screen.fill(self.white)
        font = pygame.font.Font(None, 100)
        text = font.render(f"TEAM {winner} WINS!", True, "black")
        winner_text_rect = text.get_rect()
        half_text_width = winner_text_rect.width // 2
        half_text_height = winner_text_rect.height // 2
        winner_text_x_pos = (self.window_width // 2) - half_text_width
        winner_text_y_pos = (self.window_height // 4) - half_text_height
        winner_text_rect_center = (winner_text_x_pos, winner_text_y_pos)
        self.screen.blit(text, winner_text_rect_center)
        
        font = pygame.font.Font(None, 48)
        text = font.render(f"Team Green: {green_score}", True, "black")
        green_text_rect = text.get_rect()
        half_text_width = green_text_rect.width // 2
        half_text_height = green_text_rect.height // 2
        green_text_x_pos = (self.window_width // 2) - half_text_width
        green_text_y_pos = winner_text_y_pos + (2*winner_text_rect.height)
        green_text_rect_center = (green_text_x_pos, green_text_y_pos)
        self.screen.blit(text, green_text_rect_center)
        
        font = pygame.font.Font(None, 48)
        text = font.render(f"Team Purple: {purple_score}", True, "black")
        purple_text_rect = text.get_rect()
        half_text_width = purple_text_rect.width // 2
        half_text_height = purple_text_rect.height // 2
        purple_text_x_pos = (self.window_width // 2) - half_text_width
        purple_text_y_pos = green_text_y_pos + green_text_rect.height
        purple_text_rect_center = (purple_text_x_pos, purple_text_y_pos)
        self.screen.blit(text, purple_text_rect_center)
        
        pygame.display.flip()