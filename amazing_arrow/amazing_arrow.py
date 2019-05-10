import arcade
import os
import math
import time
from models import *

INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3
GAME_WIN = 4
PLAYER_SCALING = 0.18
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Amazing Arrow"

MOVEMENT_SPEED = 5
ANGLE_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.current_state = INSTRUCTIONS_PAGE_0
        self.player_list = None
        self.player_sprite = None

        self.arrow_list = None
        self.arrow_sprite = None

        self.start_time = 0
        self.stop_time = 0

        self.score = 0
        self.dead_score = 0

        self.instructions = []
        texture = arcade.load_texture("background.png")
        self.instructions.append(texture)

    def setup(self):
        self.background = arcade.load_texture('background.png')
        self.background_over = arcade.load_texture('background_eve.png')
        self.player_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()

        self.player_sprite = Player("robin.png", PLAYER_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 150
        self.player_list.append(self.player_sprite)

        self.target = Target(600, 150)
        self.target.append_texture(
            arcade.load_texture('target.jpg', scale=0.15))
        self.target.set_texture(0)

        self.bird1 = Bird1(500, 300)
        self.bird1.append_texture(
            arcade.load_texture('bird1.png', scale=0.2))
        self.bird1.set_texture(0)

        self.bird2 = Bird2(300, 350)
        self.bird2.append_texture(
            arcade.load_texture('bird2.png', scale=0.1))
        self.bird2.set_texture(0)

        self.set_mouse_visible(False)

    def draw_instruction_page(self, page_number):
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)
        output = "AMAZING ARROW"
        arcade.draw_text(output, 150, 400, arcade.color.WHITE, 54)

        output = "Click to Start"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def draw_game_over(self):
        self.background_over = arcade.load_texture("background_eve.png")
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def draw_game_win(self):
        output = "You Win"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def on_draw(self):

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instruction_page(0)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            # if self.score == 10:
            #     self.current_state == GAME_WIN
            #     self.draw_game_win()
            #     self.score = 0
            # else:
            self.current_state == GAME_OVER
            self.draw_game_over()
            self.score = 0

    def draw_game(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text(str(self.score),
                         self.width//2, self.height - 30,
                         arcade.color.WHITE, 20)
        self.arrow_list.draw()
        self.player_list.draw()
        self.target.draw()
        self.bird1.draw()
        self.bird2.draw()

    def update(self, delta_time):

        if self.current_state == GAME_RUNNING:
            self.player_list.update()
            self.target.update()
            self.arrow_list.update()
            self.bird1.update()
            self.bird2.update()

            hit_list = arcade.check_for_collision_with_list(
                self.target, self.arrow_list)
            for arrow in hit_list:
                arrow.kill()
                self.score += 10

            hit_b1_list = arcade.check_for_collision_with_list(
                self.bird1, self.arrow_list)
            for arrow in hit_b1_list:
                # if Bird1.center_x-<Arrow.center_x <
                arrow.kill()
                self.dead_score += 1
                self.current_state = GAME_OVER

            hit_b2_list = arcade.check_for_collision_with_list(
                self.bird2, self.arrow_list)
            for arrow in hit_b2_list:
                arrow.kill()
                self.dead_score += 1
                self.current_state = GAME_OVER
            if self.score > 9:
                self.current_state == GAME_WIN

    def on_mouse_press(self, x, y, button, modifiers):

        # if self.current_state == INSTRUCTIONS_PAGE_0:
        #     self.current_state = INSTRUCTIONS_PAGE_1
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_WIN:
            self.setup()
            self.current_state == GAME_RUNNING

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.player_sprite.change_angle = ANGLE_SPEED
            self.arrow_sprite.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -ANGLE_SPEED
            self.arrow_sprite.change_angle = -ANGLE_SPEED
        if key == arcade.key.SPACE:
            self.start_time = time.time()

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
            self.arrow_sprite.change_angle = 0
        if key == arcade.key.SPACE:
            self.stop_time = time.time()
            arrow = Arrow(100, 150, 'arrow.png', 0.3)
            arrow.release(self.start_time, self.stop_time)
            arrow.angle = self.player_sprite.angle
            self.arrow_list.append(arrow)
            for i in self.arrow_list.sprite_list:
                print('x = ', i.center_x, ' y = ', i.center_y)


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
    # edit
