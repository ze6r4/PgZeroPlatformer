from pgzero.actor import Actor
from random import randint
from Hero import Hero

class Platform:

    LEFT_PLATFORM = 0
    CENTER_PLATFORM = 1
    RIGHT_PLATFORM = 2
    HALF_HEIGHT_OF_PLATFORM = 64/2
    WIDTH = 600
    HEIGHT = 800

    margin = 108
    width_of_platform = 128
    x_1 = margin
    x_2 = WIDTH/2
    x_3 = WIDTH - margin

    global x_poses
    x_poses = [x_1,x_2,x_3]

    half_of_hero = Hero.stand_actor.height/2

    y_1 = HEIGHT- HALF_HEIGHT_OF_PLATFORM
    y_2 = HEIGHT - (HALF_HEIGHT_OF_PLATFORM + half_of_hero)
    y_3 = HEIGHT - (HALF_HEIGHT_OF_PLATFORM + half_of_hero*2)
    y_4 = HEIGHT - (HALF_HEIGHT_OF_PLATFORM + half_of_hero*3)

    # всего есть 4 фиксированных варианта расположения платформы по горизонтали
    # и по вертикали
    def __init__(self, x_index,y_index):
        x = x_poses[x_index]  
        y = self.y_1 - self.half_of_hero * y_index      

        self.actor = Actor('background_elements/grass_small', (x,y))
        self.generate()
    
    def get_platfrom_x(index):
        return x_poses[index]
    def draw(self):
        self.actor.draw()

    def generate(self):
        if randint(0,5) == 5:
            self.add_enemy()
        if randint(0,1)==1:
            self.add_coin()
    def add_enemy(self):
        return
    def add_coin(self):
        return