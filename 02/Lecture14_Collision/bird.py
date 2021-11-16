import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.1)
RUN_SPEED_KMPH = 10.0
# 새의 크기를 10 픽셀당 10cm로, 프레임이 바뀌는 속도에 비해 이동 속도가 빨라보이지 않도록 시속 10km로 설정함
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y = random.randint(0, 1600-1), random.randint(300, 600-1)
        self.dir = random.randint(0, 1)
        self.frame = random.randint(0, 14)
        self.speed = 0
        if self.dir == 0:
            self.speed += RUN_SPEED_PPS
        elif self.dir == 1:
            self.speed -= RUN_SPEED_PPS

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += self.speed * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if self.x >= 1500:
            self.speed = -RUN_SPEED_PPS
        elif self.x <= 50:
            self.speed = RUN_SPEED_PPS