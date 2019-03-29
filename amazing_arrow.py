import arcade
from models import World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Background(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.world = World(width, height)
        # self.background = arcade.load_texture('background.jpg')
 
        arcade.set_background_color(arcade.color.GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.world.score),
                         self.width - 30, self.height - 30,
                         arcade.color.WHITE, 20)
    
    def update(self, delta):
        self.world.update(delta) 

def main():
    Background(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run
    
if __name__ == '__main__':
    window = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
