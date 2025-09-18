from pgzero.actor import Actor
from random import randint

class Platform:
    def __init__(self, pos):
        self.actor = Actor('background_elements/grass_small', pos)
        self.generate()
        print(self.actor.width)
        
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