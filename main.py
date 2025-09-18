import pgzrun
from pgzero.builtins import * 
from pgzero.clock import clock
from Game import Game

WIDTH = 600
HEIGHT = 800
TITLE = "Платформер"
game_is_on = False
CENTER = (WIDTH/2,HEIGHT/2)
start_button = Rect(250, 300, 100, 50)
exit_button = Rect(250, 400, 100, 50)
blue_color = (68,171,255)
green_color = (146,204,0)
red_color = (255,174,163)


game = Game(WIDTH, HEIGHT,clock,sounds)
   

def update():
    if game_is_on:
        game.update(keyboard)
        game.on_key_down(keyboard)
        return
def on_mouse_down(pos):
    global game_is_on
    if start_button.collidepoint(pos):
        game_is_on = True
        screen.clear()
    if exit_button.collidepoint(pos):
        exit()
    if game_is_on:
        game.click(pos)
        return
    
def draw():
    if game_is_on:
        screen.clear()
        game.draw(screen)
        return
    screen.clear()
    bg = Actor("background_elements/colored_land")
    bg.draw()
    
    screen.draw.filled_rect(start_button, green_color)
    screen.draw.rect(start_button, (255, 255, 255))
    
    screen.draw.text("PLAY", center=start_button.center, color="white")

    screen.draw.filled_rect(exit_button, red_color)
    screen.draw.rect(exit_button, (255, 255, 255))
    
    screen.draw.text("EXIT", center=exit_button.center,  color="white")
    

pgzrun.go()