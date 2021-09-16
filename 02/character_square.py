from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

walk = 1

while 1:
    if (walk == 1):
        x = 400

        while x + 21 < 800:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,90)
            x += 2
            delay(0.01)

        if (x + 21 >= 800):
            walk = 2

    if (walk == 2):
        y = 90

        while y + 46 < 600:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(779, y)
            y += 2
            delay(0.01)

            if (y + 46 >= 600):
                walk = 3

    if (walk == 3):
        x = 779
        
        while x - 21 > 0:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, 554)
            x -= 2
            delay(0.01)

            if (x - 21 <= 0):
                walk = 4

    if (walk == 4):
        y = 554

        while y > 90:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(21, y)
            y -= 2
            delay(0.01)

            if (y - 46 <= 90):
                walk = 5

    if (walk == 5):
        x = 21

        while x < 400:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x, 90)
            x += 2
            delay(0.01)

            if (x + 21 >= 400):
                walk = 1
