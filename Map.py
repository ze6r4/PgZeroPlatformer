from pgzero.actor import Actor
from pgzero.builtins import clock
from Enemy import Enemy


class Map:

    platforms = []
    enemies = []
    

    # по массиву из символов создаем платформы 
    def __init__(self, map):
        WIDTH = 1000
        HEIGHT = 800
        margin = 104
        width_of_platform = 128
        height_of_platform = 64 
        half_of_hero = Actor('player/alien_blue_stand').height/2
        between_platforms = 120


        y_index = 0
        for i in range(len(map)-1,0,-1):
            c = map[i]
            y = HEIGHT - (y_index * between_platforms) - half_of_hero
            y_index += 1
            self.is_long = False
            image = "grass_small"
            for x_index in range(len(c)):
                next_index = x_index + 1
                x = margin + width_of_platform*x_index 
                if c[x_index] in "-*":
                    if next_index >= len(c):
                        image = self._no_platform_next()
                    if next_index < len(c):
                        if c[next_index] in "-*":
                            image = self._platform_next()
                        else:
                            image = self._no_platform_next()
                    
                    platform = Actor(f"background_elements/{image}", (x,y))
                    self.platforms.append(platform)
                    if c[x_index] == '*':
                        enemy = Enemy(platform,clock)
                        self.enemies.append(enemy)
                else:
                    self.is_long = False
    def _no_platform_next(self):
        if self.is_long:
            self.is_long = False
            return "grass_right"
        return "grass_small"
    
    def _platform_next(self):
        if self.is_long == False:
            self.is_long = True
            return "grass_left"
        return "grass_mid"
                

                        
        
    