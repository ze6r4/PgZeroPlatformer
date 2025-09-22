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

    flip = False
    on_ground = False
    is_walking = False
    

    def __init__(self, start_platform,clock):
        stand_actor = Actor('player/alien_blue_stand')
        jump_actor = Actor('player/alien_blue_jump')
        walk1_actor = Actor('player/alien_blue_walk1')
        walk2_actor = Actor('player/alien_blue_walk2')

        self.actors = [stand_actor,jump_actor,walk1_actor,walk2_actor]

        stand_actor_left = Actor('player/alien_blue_stand_left')
        jump_actor_left = Actor('player/alien_blue_jump_left')
        walk1_actor_left = Actor('player/alien_blue_walk1_left')
        walk2_actor_left = Actor('player/alien_blue_walk2_left')

        self.actors_left = [stand_actor_left,jump_actor_left,walk1_actor_left,walk2_actor_left]

        self.actor =  Actor('player/alien_blue_stand')
        self.anchor = ("center", "bottom")
        self.actor.bottom = start_platform.top
        self.actor.left = start_platform.left
        self.velocity = Vector2(0, 0)
        self.clock = clock
        self.i=2
        self.clock.schedule_interval(self.change,self.ANIMATION_SPEED)
        self.clock.schedule_interval(self.stand,self.ANIMATION_SPEED)

    def update(self,keyboard,platforms):
        if keyboard.right or keyboard.left:
            self.is_walking = True
            self.walk_animation()

        if keyboard.left:
            self.actor.x -= self.speed
            self.flip = True
            self.check_collision_x(platforms)
        elif keyboard.right:
            self.actor.x += self.speed
            self.flip = False
            self.check_collision_x(platforms)
        
        if not keyboard.right and not keyboard.left and not keyboard.space:
            self.is_walking = False
            
        self.actor.y += self.velocity.y
        self.velocity.y += self.GRAVITY
        self.check_collision_y(platforms)

    # при столкновении с какой-либо платформой, если игрок "падает" на платформу,
    # то остается на ней. либо ударяется головой об платформу, если она сверху.
    def check_collision_y(self, platforms):
        platform_index = self.actor.collidelist(platforms)
        if platform_index != -1:
            platform = platforms[platform_index]
            if self.velocity.y >= 0:
                self.actor.bottom = platform.top
                self.on_ground = True
            else:
                self.actor.top = platform.bottom
            self.velocity.y = 0
            
    # при столкновении с какой-либо платформой, игрок "врезается" в платформу (с боку)
    def check_collision_x(self, platforms):
        platform_index = self.actor.collidelist(platforms)
        if platform_index != -1:
            platform = platforms[platform_index]
            if self.actor.right > platform.left and self.actor.left < platform.left:
                self.actor.right = platform.left
            elif self.actor.left < platform.right and self.actor.right > platform.right:
                self.actor.left = platform.right

    
            
    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_force 
            self.change_actor(self.JUMP_INDEX)
            self.on_ground = False
            sounds.jump.play()
        
        

    # смена изображений (вместо image используются actor для производительности анимации)
    def change_actor(self,index):
        if self.flip:
            self.actor.image = self.actors_left[index].image
        else:
            self.actor.image = self.actors[index].image
            
        self.draw()
    
    def walk_animation(self):
        if self.velocity.y != 0 or not self.on_ground: #если игрок только что прыгнул или в прыжке
            return  
        self.change_actor(self.i)
        
    
    def stand(self):
        if self.on_ground and (not self.is_walking):
            self.change_actor(self.STAND_INDEX)

    def change(self):
        self.i = 2 if self.i == 3 else 3

    def draw(self):
        self.actor.draw()


