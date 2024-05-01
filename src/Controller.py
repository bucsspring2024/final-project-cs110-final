import pygame
import random
import math
from src.Mallet import Mallet
from src.Puck import Puck
from src.Screen import Screen

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.puck = Puck(375, 380, 10)
        self.red_mallet = Mallet(350, 50, (255, 0, 0), 20, 20, 5)
        self.blue_mallet = Mallet(350, 730, (0, 0, 255), 20, 20, 5)
        self.clock = pygame.time.Clock()
        self.running = True
        self.red_score = 0
        self.blue_score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    direction = 0
                    if random.randint(-10, 10) > 0:
                        direction = 1
                    if random.randint(-10, 10) < 0:
                        direction = -1
                    self.puck.y_vel = self.puck.max_speed * direction
                elif event.key == pygame.K_1:
                    self.puck.x_vel = 2 * math.cos(math.radians(15))
                    self.puck.y_vel = -2 * math.sin(math.radians(15))
                elif event.key == pygame.K_2:
                    self.puck.x_vel = -2 * math.cos(math.radians(15))
                    self.puck.y_vel = 2 * math.sin(math.radians(15))
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.red_mallet.move("up")
        elif keys[pygame.K_s]:
            self.red_mallet.move("down")
        elif keys[pygame.K_a]:
            self.red_mallet.move("left")
        elif keys[pygame.K_d]:
            self.red_mallet.move("right")

        if keys[pygame.K_UP]:
            self.blue_mallet.move("up")
        elif keys[pygame.K_DOWN]:
            self.blue_mallet.move("down")
        elif keys[pygame.K_LEFT]:
            self.blue_mallet.move("left")
        elif keys[pygame.K_RIGHT]:
            self.blue_mallet.move("right")
        def update_game_state(self):
            self.red_mallet.update()
            self.blue_mallet.update()
            self.puck.update()

    def update_game_state(self):
        self.red_mallet.update()
        self.blue_mallet.update()
        self.puck.update()

        # Check for collisions between mallets and puck
        if pygame.sprite.collide_rect(self.red_mallet, self.puck):
            self.puck.y_vel *= -1
            self.puck.x_vel = random.uniform(-1, 1)
        if pygame.sprite.collide_rect(self.blue_mallet, self.puck):
            self.puck.y_vel *= -1
            self.puck.x_vel = random.uniform(-1, 1)

        # Check for scoring
        if self.puck.rect.y < self.red_mallet.rect.y:
            self.blue_score += 1
            self.puck.reset()
            self.red_mallet.reset()
            self.blue_mallet.reset()
        elif self.puck.rect.y > self.blue_mallet.rect.y + self.blue_mallet.height:
            self.red_score += 1
            self.puck.reset()
            self.red_mallet.reset()
            self.blue_mallet.reset()

    def draw_game_screen(self):
        self.screen.gamescreen()
        self.screen.screen.blit(self.red_mallet.image, self.red_mallet.rect)
        self.screen.screen.blit(self.blue_mallet.image, self.blue_mallet.rect)
        self.screen.screen.blit(self.puck.image, self.puck.rect)
        self.screen.display_score(self.red_score, self.blue_score)
        pygame.display.flip()

    def main_loop(self):
        while self.running:
            self.handle_events()
            self.handle_input()
            self.update_game_state()
            self.draw_game_screen()
            self.clock.tick(60)
