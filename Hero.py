from pygame.math import Vector2
from pgzero.actor import Actor
from pgzero.builtins import Rect
from pgzero.builtins import sounds

class Hero:
    speed = 5
    jump_force = -12
    
    STAND_INDEX = 0
    JUMP_INDEX = 1
    WALK1_INDEX = 2
    WALK2_INDEX = 3
    ANIMATION_SPEED = 0.2
    GRAVITY = 0.5

    _flip = False
    _on_ground = False
    _is_walking = False

    def __init__(self, start_platform,clock):
        stand_actor = Actor('player/alien_blue_stand')
        jump_actor = Actor('player/alien_blue_jump')
        walk1_actor = Actor('player/alien_blue_walk1')
        walk2_actor = Actor('player/alien_blue_walk2')

        self._actors = [stand_actor,jump_actor,walk1_actor,walk2_actor]

        stand_actor_left = Actor('player/alien_blue_stand_left')
        jump_actor_left = Actor('player/alien_blue_jump_left')
        walk1_actor_left = Actor('player/alien_blue_walk1_left')
        walk2_actor_left = Actor('player/alien_blue_walk2_left')

        self._actors_left = [stand_actor_left,jump_actor_left,walk1_actor_left,walk2_actor_left]

        self.actor =  Actor('player/alien_blue_stand')
        self.anchor = ("center", "bottom")
        self.actor.bottom = start_platform.top
        self.actor.left = start_platform.left
        self.velocity = Vector2(0, 0)
        self._clock = clock

        self._anim_index=2
        self._clock.schedule_interval(self._change_index,self.ANIMATION_SPEED)

    def update(self,keyboard,platforms):
        if keyboard.right or keyboard.left:
            self._is_walking = True
            self._walk_animation()

        if keyboard.left:
            self.actor.x -= self.speed
            self._flip = True
            self._check_collision_x(platforms)
        elif keyboard.right:
            self.actor.x += self.speed
            self._flip = False
            self._check_collision_x(platforms)
        
        elif not keyboard.space:
            self._is_walking = False
            if self._on_ground:
                self.change_actor(self.STAND_INDEX)
            
        self.actor.y += self.velocity.y
        self.velocity.y += self.GRAVITY
        self._check_collision_y(platforms)

    # при столкновении с какой-либо платформой, если игрок "падает" на платформу,
    # то остается на ней. либо ударяется головой об платформу, если она сверху.
    def _check_collision_y(self, platforms):
        platform_index = self.actor.collidelist(platforms)
        if platform_index != -1:
            platform = platforms[platform_index]
            if self.velocity.y >= 0:
                self.actor.bottom = platform.top
                self._on_ground = True
            else:
                self.actor.top = platform.bottom
            self.velocity.y = 0
            
    # при столкновении с какой-либо платформой, игрок "врезается" в платформу (с боку)
    def _check_collision_x(self, platforms):
        platform_index = self.actor.collidelist(platforms)
        if platform_index != -1:
            platform = platforms[platform_index]
            if self.actor.right > platform.left and self.actor.left < platform.left:
                self.actor.right = platform.left
            elif self.actor.left < platform.right and self.actor.right > platform.right:
                self.actor.left = platform.right
                

    # "уменьшаем" размеры героя для менее строгой проверки столкновения 
    def get_collider(self,w,h):
        collision_width = int(self.actor.width * w)  
        collision_height = int(self.actor.height * h)
        hero_collider = Rect(0,0,collision_width,collision_height)
        hero_collider.center =(self.actor.x,self.actor.y)
        return hero_collider
    def _platform_to_rect(self,platform):
        rect = Rect(0,0,platform.width,platform.height)
        rect.center = (platform.x,platform.y)
        return rect
    def jump(self):
        if self._on_ground:
            self.velocity.y = self.jump_force 
            self.change_actor(self.JUMP_INDEX)
            self._on_ground = False
            sounds.jump.play()

    # смена изображений (вместо image используются actor для производительности анимации)
    def change_actor(self,index):
        if self._flip:
            self._actors_left[index].pos = self.actor.pos
            self.actor = self._actors_left[index]
        else:
            self._actors[index].pos = self.actor.pos
            self.actor = self._actors[index]
            
        self.draw()
    
    def _walk_animation(self):
        #если игрок только что прыгнул или в прыжке
        if self.velocity.y != 0 or not self._on_ground: 
            return  
        self.change_actor(self._anim_index)

    #для смены кадров
    def _change_index(self):
        self._anim_index = 2 if self._anim_index == 3 else 3

    def draw(self):
        self.actor.draw()