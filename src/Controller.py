import pygame
import random
import math

from src.Puck import Puck
from src.Bumper import Bumper

class Controller:
    """
    Class representing the main controller for the game.

    Attributes:
    green_score (int): The initial score for the green team.
    purple_score (int): The initial score for the purple team.
    window_width (int): The width of the game window.
    window_height (int): The height of the game window.
    white (tuple): RGB values representing the color white.
    screen (pygame.Surface): The game window surface.
    puck (Puck): The puck object in the game.
    sample_bumper (Bumper): A sample bumper used for initialization.
    green_bumper (Bumper): The bumper for the green team.
    purple_bumper (Bumper): The bumper for the purple team.
    green_score (int): The current score of the green team.
    purple_score (int): The current score of the purple team.
    allsprites (pygame.sprite.Group): A group containing all game sprites.
    state (str): The current state of the game ("HOME", "GAME", "END", or "QUIT").
    """
    def __init__(self, green_score=0, purple_score=0):
        """
        Initializes the game controller with optional initial scores.

        Parameters:
        green_score (int): The initial score for the green team (default is 0).
        purple_score (int): The initial score for the purple team (default is 0).
        """
        pygame.init()
        buffer = 10
        puck_radius = 30
        self.window_width = 750
        self.window_height = 800
        self.white = (255, 255, 255)
        
        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.puck = Puck(self.window_width / 2 - (puck_radius / 2), self.window_height / 2 - (puck_radius / 2), puck_radius)
        self.sample_bumper = Bumper()
        self.green_bumper = Bumper((self.window_width / 2) - (self.sample_bumper.width / 2), buffer, "green")
        self.purple_bumper = Bumper((self.window_width / 2) - (self.sample_bumper.width / 2), (self.window_height - buffer - self.sample_bumper.height), "purple")
        
        self.green_score = green_score
        self.purple_score = purple_score
        
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(self.puck)
        self.allsprites.add(self.green_bumper)
        self.allsprites.add(self.purple_bumper)
        
        self.state = "HOME"
        
    def startscreenloop(self):
        """

        Game loop for the start screen.

        Displays information about the game and waits for user input to start or quit.
        """
        while self.state == "HOME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "GAME"
                    if event.key == pygame.K_ESCAPE:
                        self.state = "QUIT"

            self.screen.fill(self.white)
            font = pygame.font.Font(None, 100)
            text = font.render("Air Hockey Mania", True, "black")
            intro_text_rect = text.get_rect()
            half_text_width = intro_text_rect.width // 2
            half_text_height = intro_text_rect.height // 2
            intro_text_x_pos = (self.window_width // 2) - half_text_width
            intro_text_y_pos = (self.window_height // 4) - half_text_height
            intro_text_rect_center = (intro_text_x_pos, intro_text_y_pos)
            self.screen.blit(text, intro_text_rect_center)

            space_bw_text = 30
            font = pygame.font.Font(None, 30)
            text = font.render("Instructions:", True, "black")
            instru_text_x_pos = 0
            instru_text_y_pos = self.window_height - (self.window_height / 3)
            self.screen.blit(text, (instru_text_x_pos, instru_text_y_pos))
            text = font.render("Team Green: use the a, d, w, s keys to move your bumper", True, "black")
            instrupurple_text_x_pos = 0
            instrupurple_text_y_pos = instru_text_y_pos + space_bw_text
            self.screen.blit(text, (instrupurple_text_x_pos, instrupurple_text_y_pos))
            text = font.render("Team Purple: use the arrow keys to move your bumper", True, "black")
            instrugreen_text_x_pos = 0
            instrugreen_text_y_pos = instrupurple_text_y_pos + space_bw_text
            self.screen.blit(text, (instrugreen_text_x_pos, instrugreen_text_y_pos))
            text = font.render("Try to get the puck past the opposing team's bumper", True, "black")
            instrugoal_text_x_pos = 0
            instrugoal_text_y_pos = instrugreen_text_y_pos + space_bw_text
            self.screen.blit(text, (instrugoal_text_x_pos, instrugoal_text_y_pos))
            text = font.render("First team to 3 points wins!", True, "black")
            instruwin_text_x_pos = 0
            instruwin_text_y_pos = instrugoal_text_y_pos + space_bw_text
            self.screen.blit(text, (instruwin_text_x_pos, instruwin_text_y_pos))
            text = font.render("Press space to start each round", True, "black")
            instrustart_text_x_pos = 0
            instrustart_text_y_pos = instruwin_text_y_pos + space_bw_text
            self.screen.blit(text, (instrustart_text_x_pos, instrustart_text_y_pos))
            
            pygame.display.flip()

    def score(self):
        """
        Displays the current scores on the game window.
         """
        font = pygame.font.Font(None, 48)
        self.green_score_text = font.render(f"{self.green_score}", True, "green")
        self.purple_score_text = font.render(f"{self.purple_score}", True, "purple")
        self.screen.blit(self.green_score_text, (3, self.window_height / 4))
        self.screen.blit(self.purple_score_text, (self.window_width - 20, 3 * (self.window_height / 4)))
        
    def gameloop(self):   
        """
        Main game loop for the gameplay.

        Handles user input, updates game state, and checks for game-ending conditions.
        """
        game_to = 3    
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        direction = 0 
                        if random.randint(-10, 10) > 0:
                            direction = 1
                        if random.randint(-10, 10) < 0:
                            direction = -1
                        self.puck.y_vel = self.puck.max_vel * direction
                    if event.key == pygame.K_1:
                        self.puck.x_vel = 2 * math.cos(math.radians(15))
                        self.puck.y_vel = - 2 * math.sin(math.radians(15))
                    if event.key == pygame.K_2:
                        self.puck.x_vel = - 2 * math.cos(math.radians(15))
                        self.puck.y_vel = 2 * math.sin(math.radians(15))
                    if event.key == pygame.K_ESCAPE:
                        self.state = "QUIT"
                    if event.key == pygame.K_a:
                        self.green_bumper.move("left", None)
                    if event.key == pygame.K_d:
                        self.green_bumper.move("right", None)
                    if event.key == pygame.K_w:
                        self.green_bumper.move(None, "up")
                    if event.key == pygame.K_s:
                        self.green_bumper.move(None, "down")
                    if event.key == pygame.K_LEFT:
                        self.purple_bumper.move("left", None)
                    if event.key == pygame.K_RIGHT:
                        self.purple_bumper.move("right", None)
                    if event.key == pygame.K_UP:
                        self.purple_bumper.move(None, "up")
                    if event.key == pygame.K_DOWN:
                        self.purple_bumper.move(None, "down")
            if self.green_score >= game_to or self.purple_score >= game_to:
                self.state = "END"
                    
            
            self.screen.fill(self.white)
            pygame.draw.line(self.screen, "black", (0, self.window_height / 2), (self.window_width, self.window_height / 2), 2)
            self.allsprites.draw(self.screen)
            self.puck.move()
            self.score()
            
            if self.green_bumper.rect.x < 0:
                self.green_bumper.rect.x = 0
            if self.green_bumper.rect.x > self.window_width - self.green_bumper.width:
                self.green_bumper.rect.x = self.window_width - self.green_bumper.width
            if self.green_bumper.rect.y < 0:
                self.green_bumper.rect.y = 0
            if self.green_bumper.rect.y > self.window_height - self.green_bumper.height:
                self.green_bumper.rect.y = self.window_height - self.green_bumper.height
                
            if self.purple_bumper.rect.x < 0:
                self.purple_bumper.rect.x = 0
            if self.purple_bumper.rect.x > self.window_width - self.purple_bumper.width:
                self.purple_bumper.rect.x = self.window_width - self.purple_bumper.width
            if self.purple_bumper.rect.y < 0:
                self.purple_bumper.rect.y = 0
            if self.purple_bumper.rect.y > self.window_height - self.purple_bumper.height:
                self.purple_bumper.rect.y = self.window_height - self.purple_bumper.height
                
            if pygame.sprite.collide_rect(self.puck, self.purple_bumper):
                self.puck.y_vel *= -1
                self.puck.x_vel = random.uniform(-1, 1)
            if pygame.sprite.collide_rect(self.puck, self.green_bumper):
                self.puck.y_vel *= -1
                self.puck.x_vel = random.uniform(-1, 1)
                
             
            if self.puck.rect.x < 0:
                self.puck.x_vel *= -1
            if self.puck.rect.x > self.window_width - self.puck.radius:
                self.puck.x_vel *= -1
                
            if self.puck.rect.y < 0:
                self.purple_score += 1
                self.puck.reset()
                self.green_bumper.reset()
                self.purple_bumper.reset()
            if self.puck.rect.y > self.window_height:
                self.green_score += 1
                self.puck.reset()
                self.green_bumper.reset()
                self.purple_bumper.reset()
                
            pygame.display.flip()

    def endscreenloop(self):
        """
        Game loop for the end screen.

        Displays the winner and final scores.
        """  
        new_result = f"PREVIOUS GAME FINAL SCORE: Purple: {self.purple_score} Green: {self.green_score}"
        try:
            with open("previousscore.txt", "r") as fptr:
                old_result = fptr.read()
        except FileNotFoundError as e:
            old_result = None
        with open("previousscore.txt", "w") as fptr:
                fptr.write(new_result)
                
                
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
            
            if self.green_score >= self.purple_score:
                winner = "Green"
            elif self.green_score <= self.purple_score:
                winner = "Purple"
                
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
            
            font = pygame.font.Font(None, 60)
            text = font.render(f"FINAL SCORE: Purple: {self.purple_score} Green: {self.green_score}", True, "black")
            score_text_rect = text.get_rect()
            half_text_width = score_text_rect.width // 2
            half_text_height = score_text_rect.height // 2
            score_text_x_pos = (self.window_width // 2) - half_text_width
            score_text_y_pos = (self.window_height // 4) - half_text_height + 60
            score_text_rect_center = (score_text_x_pos, score_text_y_pos)
            self.screen.blit(text, score_text_rect_center)
            
            pygame.display.flip()

    def mainloop(self):
        """
        Main loop controlling the overall flow of the game.

        Switches between different game states (HOME, GAME, END) until the user chooses to quit.
        """
        while self.state != "QUIT":
            if self.state == "HOME":
                self.startscreenloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endscreenloop()
            else:
                print("Invalid state")