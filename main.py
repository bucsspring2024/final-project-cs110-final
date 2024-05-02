import pygame
from src.Controller import Controller #import your controller

def main():
    pygame.init()
    pygame.display.set_mode()
    game = Controller() #Create an instance on your controller object
    game.mainloop() #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()