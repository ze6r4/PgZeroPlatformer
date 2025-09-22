import pgzrun
from pgzero.builtins import * 
from pgzero.clock import clock
from Game import Game

WIDTH = 1000
HEIGHT = 800
TITLE = "Платформер"
game_is_on = False
start_button = Rect(WIDTH/2-50, HEIGHT/2-100, 100, 50)
exit_button = Rect(WIDTH/2-50, HEIGHT/2, 100, 50)

blue_color = (68,171,255)
green_color = (146,204,0)
red_color = (255,174,163)


game = Game(WIDTH, HEIGHT,clock)
music_actor = Actor("ui/music_on",(WIDTH - 30,30))
music.play("base_theme")

def update():
    if game_is_on and not game.game_over:
        game.update(keyboard)
        return
def on_mouse_down(pos):
    global game_is_on
    if start_button.collidepoint(pos):
        game.game_over = False
        game_is_on = True
        screen.clear()
    if exit_button.collidepoint(pos):
        exit()
    if music_actor.collidepoint(pos):
        music_button()
        return
def on_key_down():
    if game_is_on:
        game.on_key_down(keyboard)


def music_button():
    if music_actor.image == "ui/music_on":
        music.pause()
        music_actor.image = "ui/music_off"
    else:
        music.unpause()
        music_actor.image = "ui/music_on"

    pass
def draw():
    if game_is_on:
        screen.clear()
        game.draw(screen) 
        return
      
    draw_menu()
    

    
def draw_menu():
    screen.clear()
    bg = Actor("background_elements/colored_land")
    bg.draw()

    screen.draw.filled_rect(start_button, green_color)
    screen.draw.rect(start_button, (255, 255, 255))

    screen.draw.text("PLAY", center=start_button.center, color="white")

    screen.draw.filled_rect(exit_button, red_color)
    screen.draw.rect(exit_button, (255, 255, 255))

    screen.draw.text("EXIT", center=exit_button.center,  color="white")
    music_actor.draw()

pgzrun.go()