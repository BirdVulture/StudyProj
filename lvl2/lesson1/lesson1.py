#https://drive.google.com/drive/folders/1v1f0UO200TmzRXMd1YczYwYjEROIn1Vk?usp=drive_link
#pip install arcade
#https://pypi.org
#https://api.arcade.academy/en/latest/api/window.html#arcade.Window
#https://api.arcade.academy/en/latest/arcade.color.html
#command= для привязки функции к кнопке
import arcade
import arcade.key
import arcade.key 

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TITLE = "Пинг понг"
CHANGE_X = 5
CHANGE_Y = 5

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = -self.change_x
        if self.bottom <= 0 or self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
            
class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0
            

class Game(arcade.Window):
    def __init__ (self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('/Users/olegz/Documents/GitHub/StudyProj/lvl2/lesson1/ball.png', 0.1)
        self.bar = Bar('/Users/olegz/Documents/GitHub/StudyProj/lvl2/lesson1/bar.png', 0.1)
        self.setup()
    def setup(self):
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.ball.change_x = CHANGE_X
        self.ball.change_y = CHANGE_Y
        self.bar.center_x = SCREEN_WIDTH / 2
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bar.change_x = -CHANGE_X
        if key == arcade.key.RIGHT:
            self.bar.change_x = CHANGE_X

            
    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        
    def on_draw(self):
        #self.background_color = (255, 0, 0)
        self.clear((255, 255, 255))
        self.ball.draw()
        self.bar.draw()




window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)













arcade.run()











