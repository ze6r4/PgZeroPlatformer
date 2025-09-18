import pgzrun
from pgzero.builtins import * 
from Hero import Hero
from Platform import Platform

class Game:


    def __init__(self, width, height,clock,sounds):
        self.WIDTH = width
        self.HEIGHT = height

        margin = 88
        width_of_platform = 128
        half_height_of_platform = 64/2

        x_1 = margin
        x_2 = margin*2 + width_of_platform 
        x_3 = margin + 2*width_of_platform
        x_4 = self.WIDTH - margin

        
        self.hero = Hero((x_2, half_height_of_platform*3),clock,sounds)

        half_of_hero = self.hero.actor.height/2

        y_1 = self.HEIGHT- half_height_of_platform
        y_2 = self.HEIGHT - (half_height_of_platform + half_of_hero)
        y_3 = self.HEIGHT - (half_height_of_platform + half_of_hero*2)

        
        print(self.hero.actor.height,self.hero.actor.width)

        self.platforms = [
            Platform((x_2,y_1)), 
            Platform((x_1,y_2)),
            Platform((x_4,y_3))
        ]
        self.score = 0
        self.game_over = False
        self.bg = Actor("background_elements/blue_land")
        self.init_music()
        
    def generate_platforms(self):
        return Platform((1,1))
    def update(self, keyboard):
        if self.game_over:
            return
        if keyboard.left:
            self.hero.move_left()
        elif keyboard.right:
            self.hero.move_right()
        else:
            self.hero.stop_x()

        self.hero.update(self.platforms)

        if self.hero.actor.y > self.HEIGHT + 100:
            self.game_over = True

    def on_key_down(self, keyboard):
        if keyboard.space:
            self.hero.jump()
    
    def init_music(self):
        self.music_actor = Actor("ui/music_on",(self.WIDTH - 30,30))
        music.play("base_theme")

    def click(self,pos):
        if self.music_actor.collidepoint(pos):
            if self.music_actor.image == "ui/music_on":
                music.pause()
                self.music_actor.image = "ui/music_off"
            else:
                music.unpause()
                self.music_actor.image = "ui/music_on"

        pass

    def draw(self, screen):
        screen.clear()

        self.bg.draw()

        for platform in self.platforms:
            platform.draw()

        self.hero.draw()

        screen.draw.text(f"Score: {self.score}", (30, 10), color="black")
        self.music_actor.draw()

        if self.game_over:
            screen.draw.text(f"GAME OVER! Твой счет: {self.score}", center=(self.WIDTH/2, self.HEIGHT/2), 
                           color="black", fontsize=45)
    