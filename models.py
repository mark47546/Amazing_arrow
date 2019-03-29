import arcade

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
    
class World():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0

    def update(self, delta):
        pass