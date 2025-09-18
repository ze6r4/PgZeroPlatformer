from pygame.math import Vector2
from pgzero.actor import Actor

class Enemy:
    ANIMATION_SPEED = 0.3

    saw1 = Actor("enemy/saw_move")
    saw2 = Actor("enemy/saw")
    def __init__(self, pos,clock):
        self.actor = self.actors[self.STAND_INDEX]
        self.actor.pos = pos
        self.velocity = Vector2(0, 0)
        self.clock = clock
        self.i=2
        self.clock.schedule_interval(self.change,self.ANIMATION_SPEED)