import arcade
from models import World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.world = World(width, height)
        self.background = None
        # self.ship_sprite = ModelSprite('robin.jpg',model=self.world.robin)

    def setup(self):
        self.background = arcade.load_texture('Y1T2\\amazing_arrow\\background.png')
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2,
                                    SCREEN_WIDTH,SCREEN_HEIGHT, self.background)
        arcade.draw_text(str(self.world.score),
                         self.width - 30, self.height - 30,
                         arcade.color.WHITE, 20)
    
    def update(self, delta):
        self.world.update(delta) 

def main():
    Window(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
    
if __name__ == '__main__':
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

# class ModelSprite(arcade.Sprite):
#     def __init__(self, *args, **kwargs):
#         self.model = kwargs.pop('model', None)
 
#         super().__init__(*args, **kwargs)
 
#     def sync_with_model(self):
#         if self.model:
#             self.set_position(self.model.x, self.model.y)
 
#     def draw(self):
#         self.sync_with_model()
#         super().draw()
    
#     def sync_with_model(self):
#         if self.model:
#             self.set_position(self.model.x, self.model.y)
#             self.angle = self.model.angle

#     def update(self, delta):
#         self.world.update(delta)
#         # self.robin_sprite.set_position(self.world.robin.x, self.world.robin.y)
