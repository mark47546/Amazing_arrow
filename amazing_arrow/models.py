import arcade.key
import math
import os


class World():
    def __init__(self, width, height, angle):
        self.width = width
        self.height = height
        self.score = 0
        self.angle = 0
        self.target = Target(600,100)

    def update(self, delta):
        self.target.update()


class Player(arcade.Sprite):

    def __init__(self, image, scale):

        super().__init__(image, scale)
        self.speed = 0

    def update(self):

        angle_rad = math.radians(self.angle)

        self.angle += self.change_angle

        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class Target(arcade.Sprite):

    def __init__(self, x, y, speed=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center_x = x
        self.center_y = y
        self.ref_x = x
        self.distance = 100
        self.left_boundary = self.center_x - self.distance
        self.right_boundary = self.center_x + self.distance
        self.go_left = True
        self.speed = speed

    def update(self):
        if self.go_left == True:
            if self.center_x > self.left_boundary:
                self.center_x -= self.speed
            else:
                self.go_left = False
        elif self.go_left == False:
            if self.center_x < self.right_boundary:
                self.center_x += self.speed
            else:
                self.go_left = True

class Arrow(arcade.Sprite):

    VELOCITY_X = 4
    VELOCITY_Y = 4
    GRAVITY = 0.098

    def __init__(self, x, y,image, scale):

        super().__init__(image, scale)
        self.speed = 0
        self.vx = Arrow.VELOCITY_X
        self.vy = Arrow.VELOCITY_Y
        self.angle = 0
        self.center_x = x
        self.center_y = y

    def update(self):
        angle_rad = math.radians(self.angle)

        self.angle += self.change_angle

        self.center_x += self.vx
        self.center_y += self.vy
        self.vy -= Arrow.GRAVITY

    def release(self, start, end):
        self.vy =(end-start)+5

class Bird1(arcade.Sprite):

    def __init__(self, x, y, speed=4, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center_x = x
        self.center_y = y
        self.ref_x = x
        self.distance = 160
        self.left_boundary = self.center_x - self.distance
        self.right_boundary = self.center_x + self.distance
        self.go_left = True
        self.speed = speed

    def update(self):
        if self.go_left == True:
            if self.center_x > self.left_boundary:
                self.center_x -= self.speed
            else:
                self.go_left = False
        elif self.go_left == False:
            if self.center_x < self.right_boundary:
                self.center_x += self.speed
            else:
                self.go_left = True

class Bird2(arcade.Sprite):

    def __init__(self, x, y, speed=3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center_x = x
        self.center_y = y
        self.ref_y = y
        self.distance = 180
        self.top_boundary = self.center_y - self.distance
        self.bot_boundary = self.center_y + self.distance
        self.go_top = True
        self.speed = speed

    def update(self):
        if self.go_top == True:
            if self.center_y > self.top_boundary:
                self.center_y -= self.speed
            else:
                self.go_top = False
        elif self.go_top == False:
            if self.center_y < self.bot_boundary:
                self.center_y += self.speed
            else:
                self.go_top = True