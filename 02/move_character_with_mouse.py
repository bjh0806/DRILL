from pico2d import *
from random import randint

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
cursor_x, cursor_y = randint(0, KPU_WIDTH), randint(0, KPU_HEIGHT)
left, right = 0, 0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def cursor_move():
    global x, y
    global cursor_x, cursor_y
    if x == cursor_x and y == cursor_y:
        cursor_x, cursor_y = randint(0, KPU_WIDTH), randint(0, KPU_HEIGHT)
    pass

def boy_movex():
    global x, y
    global left, right
    if x != cursor_x:
        if x > cursor_x:
            x -= 1
            left = 1
            right = 0
        elif x < cursor_x:
            x += 1
            right = 1
            left = 0
    pass

def boy_movey():
    global x, y
    global left, right
    if y != cursor_y:
        if y > cursor_y:
            y -= 1
        elif y < cursor_y:
            y += 1
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(cursor_x, cursor_y)
    boy_movex()
    boy_movey()
    if right == 1:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif left == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    cursor_move()
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




