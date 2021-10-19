from pico2d import *
import random

# Game object class here

class BigBall:
    def __init__(self):
        self.Image = load_image('ball41x41.png')
        self.X, self.Y = random.randint(0, 800), 599

    def Update(self):
        if self.Y > 15:
            self.Y -= random.randint(1, 5)

    def Draw(self):
        self.Image.draw(self.X, self.Y)

class SmallBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 800), 599

    def update(self):
        if self.y > 15:
            self.y -= random.randint(1, 5)

    def draw(self):
        self.image.draw(self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

Big = random.randint(5, 15)

bigballs = [BigBall() for i in range(Big)]
smallballs = [SmallBall() for i in range(20 - Big)]

running = True

# game main loop code
while running:
    handle_events()

    for Ball in bigballs:
        Ball.Update()

    for ball in smallballs:
        ball.update()

    clear_canvas()

    for Ball in bigballs:
        Ball.Draw()

    for ball in smallballs:
        ball.draw()

    delay(0.01)

    update_canvas()

# finalization code