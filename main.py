import pygame
from src.Controller import Controller

def main():
    pygame.init()
    pygame.display.set_mode()
    game = Controller()
    game.main_loop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
