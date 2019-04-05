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

# class Robin(Model):
#     DIR_HORIZONTAL = 0
#     DIR_VERTICAL = 1
 
#     def __init__(self, world, x, y):
#         super().__init__(world, x, y, 0)
 
#         self.direction = Robin.DIR_VERTICAL
 
 
#     def switch_direction(self):
#         if self.direction == Robin.DIR_HORIZONTAL:
#             self.direction = Robin.DIR_VERTICAL
#             self.angle = 0
#         else:
#             self.direction = Robin.DIR_HORIZONTAL
#             self.angle = -90
 
 
#     def update(self, delta):
#         if self.direction == Robin.DIR_VERTICAL:
#             if self.y > self.world.height:
#                 self.y = 0
#             self.y += 5
#         else:
#             if self.x > self.world.width:
#                 self.x = 0
#             self.x += 5