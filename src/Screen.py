import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.window_height = 900
        self.window_width = 500
        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.white = (255,255,255)
    
    def start_screen(self):
        self.screen.fill(self.white)
        font = pygame.font.Font(None, 100)
        font = pygame.font.Font(None, 100)
        text = font.render("PADDLES", True, "black")
        intro_text_rect = text.get_rect()
        half_text_width = intro_text_rect.width // 2
        half_text_height = intro_text_rect.height // 2
        intro_text_x_pos = (self.window_width // 2) - half_text_width
        intro_text_y_pos = (self.window_height // 4) - half_text_height
        intro_text_rect_center = (intro_text_x_pos, intro_text_y_pos)
        self.screen.blit(text, intro_text_rect_center)
        
        font = pygame.font.Font(None, 48)
        text = font.render("By Daniel Sirota", True, "black")
        text_rect = text.get_rect()
        half_text_width = text_rect.width // 2
        half_text_height = text_rect.height // 2
        creators_text_x_pos = (self.window_width // 2) - half_text_width
        creators_text_y_pos = intro_text_y_pos + intro_text_rect.height
        creators_text_rect_center = (creators_text_x_pos, creators_text_y_pos)
        self.screen.blit(text, creators_text_rect_center)
        
        font = pygame.font.Font(None, 48)
        text = font.render("PRESS SPACE TO START", True, "black")
        starttext_rect = text.get_rect()
        half_text_width = starttext_rect.width // 2
        half_text_height = starttext_rect.height // 2
        starttext_x_pos = (self.window_width // 2) - half_text_width
        starttext_y_pos = self.window_height - (self.window_height // 2)
        starttext_rect_center = (starttext_x_pos, starttext_y_pos)
        self.screen.blit(text, starttext_rect_center)
        
        space_bw_text = 30
        font = pygame.font.Font(None, 48)
        text = font.render("Instructions:", True, "black")
        instru_text_x_pos = 0
        instru_text_y_pos = self.window_height - (self.window_height/3)
        self.screen.blit(text, (instru_text_x_pos, instru_text_y_pos))
        text = font.render("Team Red: use the arrow keys to move your mallet up, down, left, and right", True, "black")
        instrublue_text_x_pos = 0
        instrublue_text_y_pos = instru_text_y_pos + space_bw_text
        self.screen.blit(text, (instrublue_text_x_pos, instrublue_text_y_pos))
        text = font.render("Team Blue: use the a, w, s, and d keys to move your mallet up, down, left, and right", True, "black")
        instrured_text_x_pos = 0
        instrured_text_y_pos = instrublue_text_y_pos + space_bw_text
        self.screen.blit(text, (instrured_text_x_pos, instrured_text_y_pos))
        text = font.render("Try to get the puck in the opposing goal", True, "black")
        instrugoal_text_x_pos = 0
        instrugoal_text_y_pos = instrured_text_y_pos + space_bw_text
        self.screen.blit(text, (instrugoal_text_x_pos, instrugoal_text_y_pos))
        text = font.render("First team to score 5 times wins!", True, "black")
        instruwin_text_x_pos = 0
        instruwin_text_y_pos = instrugoal_text_y_pos + space_bw_text
        self.screen.blit(text, (instruwin_text_x_pos, instruwin_text_y_pos))
        
        pygame.display.flip()
        
    def gamescreen(self):
        self.screen.fill(self.white)
        pygame.draw.line(self.screen, "black", (0, self.window_height/2), (self.window_width, self.window_height/2), 2)
        
        pygame.display.flip()
        
    def endscreen(self, winner, redscore, bluescore):
        self.screen.fill(self.white)
        font = pygame.font.Font(None, 100)
        text = font.render(f"TEAM {winner} WINS!", True, "white")
        winner_text_rect = text.get_rect()
        half_text_width = winner_text_rect.width // 2
        half_text_height = winner_text_rect.height // 2
        winner_text_x_pos = (self.window_width // 2) - half_text_width
        winner_text_y_pos = (self.window_height // 4) - half_text_height
        winner_text_rect_center = (winner_text_x_pos, winner_text_y_pos)
        self.screen.blit(text, winner_text_rect_center)
        
        pygame.display.flip()