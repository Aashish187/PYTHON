class Settings:
    """A class to store all settings for Alien Invavsion"""
    def __init__(self):
        """Initialize game's static settings."""
        # Screen Settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        # Ship settings
        # self.ship_speed=3
        self.ship_limit=3
        # Bullet settings
        # self.bullet_speed=2.5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=5
        # Alien Settings
        # self.alien_speed=1.0
        self.fleet_drop_speed=10
        # Fleet direction of 1 represents right ; -1 represents left
        # self.fleet_direction=1
        # How quickly the game speeds up
        self.speedup_scale=1.3
        # How quickly the alien point value increases
        self.score_scale=1.5
        self.initialise_dynamic_settings()


    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game"""
        self.ship_speed=3.5
        self.bullet_speed=2.5
        self.alien_speed=1.5
        # fleet direction of 1 represent right and -1 represents left 
        self.fleet_direction=1
        # Scoring settings
        self.alien_points=50
    
    def increase_speed(self):
        """Increase speed settings and alien points"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        
        self.alien_points=int(self.alien_points*self.score_scale)
        