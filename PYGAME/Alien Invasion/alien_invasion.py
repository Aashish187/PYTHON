import sys
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        """Initialise the game, and create game resources"""
        pygame.init() # It gives the background setting for the game to work properly
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = 1200
        self.settings.screen_height = 800


        # alternative given below this
        # self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        # self.screen=pygame.display.set_mode((1200,800)) used to create a display window and the argument defines the dimensions
        pygame.display.set_caption("Alien Invasion")
        # Create an instance to store game stats and scoreboard
        self.stats=GameStats(self)
        self.sb=Scoreboard(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
        self.game_active=False
        # make the play button
        self.play_button=Button(self,"Play")

        # Set the Background color
        # self.bg_color=(230,230,230)
    def run_game(self):
        """Start the main loop for the game """
        while True:
            self._check_events()
            self._update_screen()
            if self.game_active:
            
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets"""
        # update bullet positions
        self.bullets.update()
        # Get rid of bullets that have dissappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                 self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    

    def _check_bullet_alien_collisions(self):
        """Respond to bullet alien collisions"""
        #Check for any bullet that hits the aliens
        #If so , get rid of the bullet and the alien
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score+=self.settings.alien_points*len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
        # Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            #Increase level
            self.stats.level+=1
            self.sb.prep_level()
        
    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                #Right movement
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
           
           
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings
            self.settings.initialise_dynamic_settings()
        # if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active=True
            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and centre the ship
            self._create_fleet()
            self.ship.centre_ship()
         # Hide the mouse cursor
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self,event):
        """Respond to key presses"""
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key == pygame.K_q: # Exit using q
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
         """Respond to key releases"""
         if event.key==pygame.K_RIGHT:
            self.ship.moving_right= False
         elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
         # move the ship to the right
          # self.ship.rect.x+=1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create a fleet of aliens"""
# create an alien and keep adding aliens until there's no room left
# spacing between aliens is one alien width and one alien height
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y< (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width-2*alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            # finished a row; reset x value , and increment y value
            current_x=alien_width
            current_y+=2*alien_height


    def _create_alien(self,x_position,y_position):
        """Create an alien and place it in the row"""
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1


    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
# Redraw the screen during each pass through the loop
            # self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)# using settings module
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        
            # Make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(60)


    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        # Look for aliens hitting bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left>0:
        # Decrement Ships Left,and update scoreboard
            self.stats.ships_left-=1
            self.sb.prep_ships()
        # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
        # Create a new fleet and centre the ship 
            self._create_fleet()
            self.ship.centre_ship()
        #Pause
            sleep(.5)
        else :
            self.game_active=False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """Check if any alien have reached the bottom"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit 
                self._ship_hit()
                break


if __name__=="__main__":
    # Make a game instance, and run the game
    ai=AlienInvasion()
    ai.run_game()
