import pygame
import sys
from Mallet import Mallet
from Puck import Puck

class Controller:
    def __init__(self):
        pygame.init()

        # Initialize the screen
        self.screen = pygame.display.set_mode([self.window_width, self.window_height])

        # Initialize mallets
        self.mallet_red = Mallet(350, 50, (255, 0, 0), 20, 20, 5)
        self.mallet_blue = Mallet(350, 730, (0, 0, 255), 20, 20, 5)

        # Initialize the puck
        self.puck = Puck(375, 380, 10)

        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.mallet_red.move("up")
        if keys[pygame.K_DOWN]:
            self.mallet_red.move("down")
        if keys[pygame.K_LEFT]:
            self.mallet_red.move("left")
        if keys[pygame.K_RIGHT]:
            self.mallet_red.move("right")

        if keys[pygame.K_w]:
            self.mallet_blue.move("up")
        if keys[pygame.K_s]:
            self.mallet_blue.move("down")
        if keys[pygame.K_a]:
            self.mallet_blue.move("left")
        if keys[pygame.K_d]:
            self.mallet_blue.move("right")

    def update_game_state(self):
        self.mallet_red.update()
        self.mallet_blue.update()
        self.puck.update()

        # Check for collisions between mallets and puck
        if pygame.sprite.collide_rect(self.mallet_red, self.puck):
            self.puck.xspeed *= -1
            self.puck.yspeed *= -1
        if pygame.sprite.collide_rect(self.mallet_blue, self.puck):
            self.puck.xspeed *= -1
            self.puck.yspeed *= -1

        # Check for scoring
        if self.puck.rect.y < 0 or self.puck.rect.y > self.screen.window_height:
            self.puck.reset()

    def draw_game_screen(self):
        self.screen.gamescreen()
        self.screen.screen.blit(self.mallet_red.image, self.mallet_red.rect)
        self.screen.screen.blit(self.mallet_blue.image, self.mallet_blue.rect)
        self.screen.screen.blit(self.puck.image, self.puck.rect)
        pygame.display.flip()

    def run_game(self):
        while self.running:
            self.handle_events()
            self.handle_input()
            self.update_game_state()
            self.draw_game_screen()
            self.clock.tick(60)