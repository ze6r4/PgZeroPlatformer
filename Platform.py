from pgzero.actor import Actor

class Platform:
    def __init__(self, pos, image='background_elements/grass_small'):
        self.actor = Actor(image, pos)
        
    def draw(self):
        self.actor.draw()