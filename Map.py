from pgzero.actor import Actor
from pgzero.builtins import clock
from Enemy import Enemy


class Map:

    platforms = []
    enemies = []
    stars = []

    BETWEEN_PLATFORMS_Y = 130

    # по массиву из символов создаем платформы и врагов
    # высота платформ увеличивается с каждой новой строчкой
    # если после платформы идет платформа, то нужно собрать длинную платформу.
    def __init__(self, WIDTH,HEIGHT, map):
        _margin = 104
        _width_of_platform = 128
        _height_of_platform = 64 
        _half_of_hero = Actor('player/alien_blue_stand').height/2 

        _y_index = 0
        for i in range(len(map)-1,-1,-1):
            line = map[i]
            y = HEIGHT - (_y_index * self.BETWEEN_PLATFORMS_Y) - _half_of_hero
            _y_index += 1

            self.is_long = False
            image = "grass_small"
            for x_index in range(len(line)):
                next_index = x_index + 1
                x = _margin + _width_of_platform*x_index 
                
                if line[x_index] in "-*^":
                    image = self.__check_next_platform(line,next_index)
                    platform = Actor(f"background_elements/{image}", (x,y))
                    self.platforms.append(platform)
                    if line[x_index] == '^':
                        self.__add_enemy(platform)
                    if line[x_index] == '*':
                        self.__add_star(platform)
                else:
                    self.is_long = False
    
    def __check_next_platform(self,line,next_index):
        if next_index >= len(line):
            image = self.__no_platform_next()
        if next_index < len(line):
            if line[next_index] in "-*^":
                image = self.__platform_next()
            else:
                image = self.__no_platform_next()
        return image
    
    def __add_enemy(self,platform):
        enemy = Enemy(platform,clock)
        self.enemies.append(enemy)
    def __add_star(self,platform):
        star = Actor("background_elements/star",(platform.x,platform.y - platform.height - 20))
        self.stars.append(star)

    def __no_platform_next(self):
        if self.is_long:
            self.is_long = False
            return "grass_right"
        return "grass_small"
    
    def __platform_next(self):
        if self.is_long == False:
            self.is_long = True
            return "grass_left"
        return "grass_mid"
                

                        
        
    