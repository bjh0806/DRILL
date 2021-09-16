from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while 1:
    theta = 0

    while theta < 360:
        clear_canvas_now()
        grass.draw_now(400,30)
        x = 400 + math.cos(math.radians(theta)) * 215
        y = 300 + math.sin(math.radians(theta)) * 215
        character.draw_now(x, y)
        theta += 1

    if  (theta >= 360):
        theta = 0
