import arcade
import random

from arcade import load_texture

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Animation(arcade.Sprite):
    i = 0
    time = 0
    def update_animation(self, delta_time):
        self.time += delta_time

        if self.time >= 0.1:
            self.time = 0
            if self.i == len(self.textures) - 1:
                self.i = 0
            else:
                self.i += 1
            self.set_texture(self.i)





# class Bg(arcade.Sprite):
#     def __init__(self):
#         super().__init__("images/bg.png", 1)
#         self.center_y = WINDOW_HEIGHT/2
#         self.change_x = -10
#
#     def update(self):
#         self.center_x += self.change_x
#         if self.center_x <= -WINDOW_WIDTH / 2:
#             self.center_x += 2 * WINDOW_WIDTH


class Cactus(arcade.Sprite):
    def __init__(self):
        super().__init__("images/cactus1.png", 0.5)
        self.center_y = 200
        self.change_x = -10
        # self.center_x = random.randrange(850, 1600, 250)
        self.center_x = 850


    def update(self):
        self.center_x += self.change_x
        if self.center_x <= -50:
            # self.center_x = random.randrange(850, 1600, 300)
            self.center_x = random.randint(850,1050)
            self.change_x = -10

class Dino(Animation):
    def __init__(self):
        super().__init__()
        self.textures = []
        self.center_x = 100
        self.center_y = 200
        self.change_y = 0
        self.i = 0
        self.time = 0
        self.scale = 0.5

    def append_t(self):
        self.append_texture(arcade.load_texture("images/dino1.png"))
        self.append_texture(arcade.load_texture("images/dino2.png"))
        self.append_texture(arcade.load_texture("images/dino3.png"))
        self.set_texture(0)

    def update(self):
        self.center_y += self.change_y
        if self.center_y >= 350:
            self.change_y = -4

        elif self.center_y <= 200 or self.center_y == 200:
            self.center_y = 200
            self.change_y = 0


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Dino")
        self.cactus = Cactus()
        self.dino = Dino()
        self.dino.append_t()
        self.score = 0
        self.game = "game"
        self.bg_game = load_texture("images/bg.png")
        self.bg_win = load_texture("images/win.png")
        self.bg_end = load_texture("images/game_over.png")
        # self.cacti = arcade.SpriteList()
        # self.bgs = arcade.SpriteList()

        # for x in [650, 850, 1050]:
        #     self.cacti.append(Cactus())
        #
        # for x in [WINDOW_WIDTH / 2, 3 * WINDOW_WIDTH / 2]:
        #     self.bgs.append(Bg())

    def on_draw(self):
        self.clear((0, 100, 0))


        if self.game == "game":
            # self.bgs.draw()
            arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT, self.bg_game)
            self.dino.draw()
            self.cactus.draw()
            # self.cacti.draw()

        if self.game == "lose":
            arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.bg_end)

        if self.game == "win":
            arcade.draw_texture_rectangle(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT, self.bg_win)

        arcade.draw_text(f"Score:{self.score}", 50, WINDOW_HEIGHT - 50, (0, 0, 0), 16)


    def update(self, delta_time: float):
        if self.game == "game":
            # self.cacti.update()
            # self.bgs.update()
            self.cactus.update()
            self.dino.update()
            self.dino.update_animation(delta_time)

        if self.dino.center_x == self.cactus.center_x:
            self.score += 1

        if arcade.check_for_collision(self.dino, self.cactus):
            self.game = "lose"
            self.dino.stop()
            self.cactus.stop()
            self.dino.kill()
            self.cactus.kill()

        if self.score == 20:
            self.game = "win"
            self.dino.stop()
            self.cactus.stop()
            self.dino.kill()
            self.cactus.kill()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP and self.dino.center_y == 200:
            self.dino.change_y = 15
            print(self.dino.center_y)

    def on_key_release(self, symbol: int, modifiers: int):
        if self.game != "game" and symbol == arcade.key.SPACE:
            self.restart()

    def restart(self):
        self.dino.center_y = 200
        self.dino.change_y = 0
        self.score = 0
        self.game = "game"
        # for i, x in enumerate([650, 850, 1050]):
        #     self.cacti[i].center_x = x
        # for i, x in enumerate([400,1200]):
        #     self.bgs[i].center_x = x


window = Game()
arcade.run()

# доделать игру поиграться с фуллскрином