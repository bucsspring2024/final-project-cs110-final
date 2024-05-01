import pygame
import random
import math

from src.Puck import Puck
from src.Bumper import Bumper

class Controller:
    """
    Class representing the main controller for the game.

    Attributes:
    red_score (int): The initial score for the red team.
    blue_score (int): The initial score for the blue team.
    window_width (int): The width of the game window.
    window_height (int): The height of the game window.
    green (tuple): RGB values representing the color green.
    screen (pygame.Surface): The game window surface.
    ball (Ball): The ball object in the game.
    sample_paddle (Paddle): A sample paddle used for initialization.
    red_paddle (Paddle): The paddle for the red team.
    blue_paddle (Paddle): The paddle for the blue team.
    red_score (int): The current score of the red team.
    blue_score (int): The current score of the blue team.
    allsprites (pygame.sprite.Group): A group containing all game sprites.
    state (str): The current state of the game ("HOME", "GAME", "END", or "QUIT").
    """
    def __init__(self, red_score=0, blue_score=0):
        """
        Initializes the game controller with optional initial scores.

        Parameters:
        red_score (int): The initial score for the red team (default is 0).
        blue_score (int): The initial score for the blue team (default is 0).
        """
        pygame.init()
        buffer = 10
        ball_radius = 30
        self.window_width = 750
        self.window_height = 800
        self.white = (255, 255, 255)
        

        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.ball = Puck(self.window_width / 2 - (ball_radius / 2), self.window_height / 2 - (ball_radius / 2), ball_radius)
        self.sample_paddle = Bumper()
        self.red_paddle = Bumper((self.window_width / 2) - (self.sample_paddle.width / 2), buffer, "red")
        self.blue_paddle = Bumper((self.window_width / 2) - (self.sample_paddle.width / 2), (self.window_height - buffer - self.sample_paddle.height), "blue")

        
        self.red_score = red_score
        self.blue_score = blue_score
        
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(self.ball)
        self.allsprites.add(self.red_paddle)
        self.allsprites.add(self.blue_paddle)
        
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
            text = font.render("Team Red: use the a and d keys to move your bumper left and right", True, "black")
            instrublue_text_x_pos = 0
            instrublue_text_y_pos = instru_text_y_pos + space_bw_text
            self.screen.blit(text, (instrublue_text_x_pos, instrublue_text_y_pos))
            text = font.render("Team Blue: use the arrow keys to move your bumper left and right", True, "black")
            instrured_text_x_pos = 0
            instrured_text_y_pos = instrublue_text_y_pos + space_bw_text
            self.screen.blit(text, (instrured_text_x_pos, instrured_text_y_pos))
            text = font.render("Try to get the puck past the opposing teams bumper", True, "black")
            instrugoal_text_x_pos = 0
            instrugoal_text_y_pos = instrured_text_y_pos + space_bw_text
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
        self.red_score_text = font.render(f"{self.red_score}", True, "red")
        self.blue_score_text = font.render(f"{self.blue_score}", True, "blue")
        self.screen.blit(self.red_score_text, (3, self.window_height / 4))
        self.screen.blit(self.blue_score_text, (self.window_width - 20, 3 * (self.window_height / 4)))
        
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
                        self.ball.y_vel = self.ball.max_vel * direction
                    if event.key == pygame.K_1:
                        self.ball.x_vel = 2 * math.cos(math.radians(15))
                        self.ball.y_vel = - 2 * math.sin(math.radians(15))
                    if event.key == pygame.K_2:
                        self.ball.x_vel = - 2 * math.cos(math.radians(15))
                        self.ball.y_vel = 2 * math.sin(math.radians(15))
                    if event.key == pygame.K_ESCAPE:
                        self.state = "QUIT"
                    if event.key == pygame.K_a:
                        self.red_paddle.move("left")
                    if event.key == pygame.K_d:
                        self.red_paddle.move("right")
                    if event.key == pygame.K_LEFT:
                        self.blue_paddle.move("left")
                    if event.key == pygame.K_RIGHT:
                        self.blue_paddle.move("right")
            if self.red_score >= game_to or self.blue_score >= game_to:
                self.state = "END"
                    
            
            self.screen.fill(self.white)
            pygame.draw.line(self.screen, "black", (0, self.window_height / 2), (self.window_width, self.window_height / 2), 2)
            self.allsprites.draw(self.screen)
            self.ball.move()
            self.score()
            
            if self.red_paddle.rect.x < 0:
                self.red_paddle.rect.x = 0
            if self.red_paddle.rect.x > self.window_width - self.red_paddle.width:
                self.red_paddle.rect.x = self.window_width - self.red_paddle.width
            if self.blue_paddle.rect.x < 0:
                self.blue_paddle.rect.x = 0
            if self.blue_paddle.rect.x > self.window_width - self.blue_paddle.width:
                self.blue_paddle.rect.x = self.window_width - self.blue_paddle.width
            
            if pygame.sprite.collide_rect(self.ball, self.blue_paddle):
                self.ball.y_vel *= -1
                self.ball.x_vel = random.uniform(-1, 1)
            if pygame.sprite.collide_rect(self.ball, self.red_paddle):
                self.ball.y_vel *= -1
                self.ball.x_vel = random.uniform(-1, 1)
                
             
            if self.ball.rect.x < 0:
                self.ball.x_vel *= -1
            if self.ball.rect.x > self.window_width - self.ball.radius:
                self.ball.x_vel *= -1
                
            if self.ball.rect.y < self.red_paddle.rect.y:
                self.blue_score += 1
                self.ball.reset()
                self.red_paddle.reset()
                self.blue_paddle.reset()
            if self.ball.rect.y > self.blue_paddle.rect.y + self.blue_paddle.height:
                self.red_score += 1
                self.ball.reset()
                self.red_paddle.reset()
                self.blue_paddle.reset()
                
            pygame.display.flip()

    def endscreenloop(self):
        """
        Game loop for the end screen.

        Displays the winner and final scores.
        """  
        new_result = f"PREVIOUS GAME FINAL SCORE: Blue: {self.blue_score} Red: {self.red_score}"
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
            
            if self.red_score >= self.blue_score:
                winner = "RED"
            elif self.red_score <= self.blue_score:
                winner = "BLUE"
                
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
            text = font.render(f"FINAL SCORE: Blue: {self.blue_score} Red: {self.red_score}", True, "black")
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