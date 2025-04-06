import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""
    def __init__(self,ai_game):
        """Initialise the ship and set it's starting position"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
    # Load the ship image and get its rect
        self.image=pygame.image.load('D:/coding/PYTHON PROJECTS/alien_invasion/ship.bmp')
        self.rect=self.image.get_rect()
    # start each new ship at the bottom centre of the screen
        self.rect.midbottom=self.screen_rect.midbottom
        # store a float for horizontal position
        self.x=float(self.rect.x)

        # movement flag; start with a ship that is not moving
        self.moving_right=False
        self.moving_left=False
    def update(self):
        """Update the ships position based on the movement flag"""
        # update the ships x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.x+=1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            # self.rect.x-=1
            self.x -= self.settings.ship_speed
        # update rect object from self.x
        self.rect.x=self.x


    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image,self.rect)

    def centre_ship(self):
        """Centre the ship on the screen """
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
