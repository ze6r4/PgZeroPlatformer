from pygame.math import Vector2
from pgzero.actor import Actor
from random import randint

class Enemy:
    global ANIMATION_SPEED
    ANIMATION_SPEED = 0.2
    speed = 1.5
    saw = Actor("enemy/saw_half")
    saw1 = Actor("enemy/saw_half")
    saw2 = Actor("enemy/saw_half_move")
    change_index = 0
    def __init__(self, platform,clock):
        self.saw.bottomleft = platform.topleft
        self.saw.y +=5  #для столкновений с платформой опускаем чуть пониже
        clock.schedule_interval(self.idle_animation,ANIMATION_SPEED)
        
    def update(self,platforms):
        self.saw.x += self.speed
        
        for platform in platforms:
            if self.saw.colliderect(platform):  
                #создание точки рядом с пилой для поиска соседних платформ
                if self.speed > 0:
                    check_point = (self.saw.right + 15, platform.top + 5) 
                else:
                    check_point = (self.saw.left - 15, platform.top + 5) 
                
                has_next_platform = any(p.collidepoint(check_point) for p in platforms if p != platform)
                
                if not has_next_platform:
                    if self._on_the_end_of_platform(platform):
                        self.speed = -self.speed
                        self.saw.x += self.speed
                break
    def _on_the_end_of_platform(self,platform):
        return (self.speed > 0 and self.saw.right >= platform.right - 5) or \
                    (self.speed < 0 and self.saw.left <= platform.left + 5)
    def idle_animation(self):
        if self.change_index == 0:
            self.saw2.pos = self.saw.pos
            self.saw = self.saw2
            self.change_index=1
        else:
            self.saw1.pos = self.saw.pos
            self.saw = self.saw1
            self.change_index=0
    def draw(self):
        self.saw.draw()
            