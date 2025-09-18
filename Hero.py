from pygame.math import Vector2
from pgzero.actor import Actor

class Hero:
    speed = 5
    jump_force = -15
    
    stand_actor = Actor('player/alien_blue_stand')
    jump_actor = Actor('player/alien_blue_jump')
    walk1_actor = Actor('player/alien_blue_walk1')
    walk2_actor = Actor('player/alien_blue_walk2')
    actors = [stand_actor,jump_actor,walk1_actor,walk2_actor]

    stand_actor_left = Actor('player/alien_blue_stand_left')
    jump_actor_left = Actor('player/alien_blue_jump_left')
    walk1_actor_left = Actor('player/alien_blue_walk1_left')
    walk2_actor_left = Actor('player/alien_blue_walk2_left')
    actors_left = [stand_actor_left,jump_actor_left,walk1_actor_left,walk2_actor_left]

    STAND_INDEX = 0
    JUMP_INDEX = 1
    WALK1_INDEX = 2
    WALK2_INDEX = 3

    ANIMATION_SPEED = 0.2

    image_counter = 0
    do_walk = False
    GRAVITY = 0.5

    flip = False
    on_ground = True
    

    def __init__(self, pos,clock,sounds):
        self.actor = self.actors[self.STAND_INDEX]
        self.actor.pos = pos
        self.velocity = Vector2(0, 0)
        self.clock = clock
        self.i=2
        self.clock.schedule_interval(self.change,self.ANIMATION_SPEED)
        self.sounds = sounds
        

    def update(self, platforms):
        self.velocity.y += self.GRAVITY
        self.actor.x += self.velocity.x
        self.check_collision_x(platforms)
        
        self.actor.y += self.velocity.y
        self.check_collision_y(platforms)

        if self.velocity.x == 0:
            self.change_actor(self.STAND_INDEX) 
        
        
    # при столкновении с какой-либо платформой, если игрок "падает" на платформу,
    # то остается на ней. либо ударяется головой об платформу, если она сверху.
    def check_collision_y(self, platforms):
        for platform in platforms:
            if self.actor.colliderect(platform.actor):
                if self.velocity.y > 0:
                    if self.actor.y < platform.actor.y:
                        self.actor.bottom = platform.actor.top
                    self.on_ground = True
                    self.velocity.y = 0
                elif self.velocity.y == 0:
                    if self.velocity.x == 0 and self.on_ground == 0:
                        self.change_actor(self.STAND_INDEX)
                else:
                    if self.actor.y > platform.actor.y:
                        self.actor.top = platform.actor.bottom
                

                break
    # при столкновении с какой-либо платформой, игрок "врезается" в платформу (с боку)
    def check_collision_x(self, platforms):
        for platform in platforms:
            if self.actor.colliderect(platform.actor):
                if self.velocity.x > 0:
                    self.actor.right = platform.actor.left
                elif self.velocity.x < 0:
                    self.actor.left = platform.actor.right
                self.stop_x()
                break

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_force 
            self.change_actor(self.JUMP_INDEX) # 1 - jump actor
            self.on_ground = False
            self.sounds.jump.play()
        else:
            return
        
    def move_left(self):
        i = 2
        self.velocity.x = -1*self.speed 
        self.flip = True    
        self.walk_animation()

    def move_right(self):
        self.velocity.x = self.speed
        self.flip = False
        self.walk_animation()
        

    # принудительно останавливает движение по горизонтали 
    def stop_x(self):
        self.velocity.x = 0
        

    # смена изображений (вместо image используются actor для производительности анимации)
    def change_actor(self,index):
        if self.flip:
            self.actors_left[index].pos = self.actor.pos
            self.actor = self.actors_left[index]
        else:
            self.actors[index].pos = self.actor.pos
            self.actor = self.actors[index]
    
    def walk_animation(self):
        if self.velocity.y != 0: #если игрок только что прыгнул
            return
        i = self.i
        self.change_actor(i)
        
        
    def change(self):
        self.i = 2 if self.i == 3 else 3

    def draw(self):
        self.actor.draw()

