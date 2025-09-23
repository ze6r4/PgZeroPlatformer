from pygame.math import Vector2
from pgzero.actor import Actor
from random import randint

class Enemy:
    global ANIMATION_SPEED
    ANIMATION_SPEED = 0.2
    SPEED = 1.7

    change_index = 0
    def __init__(self, platform,clock):
        
        self.saw = Actor("enemy/saw_half")
        self._saw1 = Actor("enemy/saw_half")
        self._saw2 = Actor("enemy/saw_half_move")

        self.saw.bottomleft = platform.topleft
        #для столкновений с платформой опускаем чуть пониже
        self.saw.y +=5 
        clock.schedule_interval(self._idle_animation,ANIMATION_SPEED)
        
    def update(self,platforms):
        self.saw.x += self.SPEED
        for platform in platforms:
            if self.saw.colliderect(platform):  
                #создание точки рядом с пилой для поиска соседних платформ
                if self.SPEED > 0:
                    check_point = (self.saw.right + 15, platform.top + 5) 
                else:
                    check_point = (self.saw.left - 15, platform.top + 5) 
                
                has_next_platform = any(p.collidepoint(check_point) for p in platforms if p != platform)
                
                if not has_next_platform:
                    if self.__on_the_end_of_platform(platform):
                        self.SPEED = -self.SPEED
                        self.saw.x += self.SPEED
                break
    def __on_the_end_of_platform(self,platform):
        return (self.SPEED > 0 and self.saw.right >= platform.right - 5) or \
                    (self.SPEED < 0 and self.saw.left <= platform.left + 5)
    def _idle_animation(self):
        if self.change_index == 0:
            self._saw2.pos = self.saw.pos
            self.saw = self._saw2
            self.change_index=1
        else:
            self._saw1.pos = self.saw.pos
            self.saw = self._saw1
            self.change_index=0
    def draw(self):
        self.saw.draw()
            