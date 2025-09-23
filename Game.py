import pgzrun
from pgzero.builtins import * 
from Hero import Hero
from Map import Map
from Enemy import Enemy

class Game:
    
    def __init__(self, width, height,clock):
        self.WIDTH = width
        self.HEIGHT = height
        self.clock = clock
        self.create_game()
        
    def create_game(self):
        # 0 ничего нет
        # - простая платформа 
        # * платформа с пилой
        platforms_map = ["000---",
                         "00-000",
                         "-00000",
                         "0-*--00",
                         "000000-",
                         "0000--0"]
        
        map = Map(platforms_map)
        self.platforms = map.platforms
        self.enemies = map.enemies

        self.hero = Hero(self.platforms[0],self.clock)
        self.score = 0
        self.game_over = False
        self.bg = Actor("background_elements/blue_land")

    def update(self, keyboard):
        if self.game_over:
            return
        for enemy in self.enemies:
            enemy.update(self.platforms)

        self.hero.update(keyboard, self.platforms)
        self._check_player_fall()
        self._check_collision_enemy(self.enemies)
        

    def _check_collision_enemy(self,enemies):
        for enemy in enemies:
            if self.hero.actor.colliderect(enemy.saw):
                collision_width = int(self.hero.actor.width * 0.7)  
                collision_height = int(self.hero.actor.height * 0.96)
                # "уменьшаем" размеры героя для менее строгой проверки столкновения 
                hero_collider = Rect(0,0,collision_width,collision_height)
                hero_collider.center =(self.hero.actor.x,self.hero.actor.y)
                saw_collider = Rect(0,0,enemy.saw.width,enemy.saw.height)
                saw_collider.center = (enemy.saw.x,enemy.saw.y)
                if hero_collider.colliderect(saw_collider):
                    self.game_over = True
            

    def _check_player_fall(self):
        if self.hero.actor.y > self.HEIGHT + 100:
            self.game_over = True

    def on_key_down(self, keyboard):
        if keyboard.space:
            self.hero.jump()

    def draw(self, screen):
        screen.clear()

        self.bg.draw()

        for platform in self.platforms:
            platform.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.hero.draw()
        if self.game_over:
            self._draw_game_over(screen)
            
    def _draw_game_over(self,screen):
        screen.draw.text(f"GAME OVER! Твой счет: {self.score}", center=(self.WIDTH/2, self.HEIGHT/2), 
                        color="black", fontsize=45)
        return
        
    