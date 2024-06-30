#https://drive.google.com/drive/folders/1v1f0UO200TmzRXMd1YczYwYjEROIn1Vk?usp=drive_link
#pip install arcade
#https://pypi.org
#https://api.arcade.academy/en/latest/api/window.html#arcade.Window
#https://api.arcade.academy/en/latest/arcade.color.html
import arcade 

class Ball(arcade.Sprite):
       pass

class Game(arcade.Window):
    def __init__ (self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('/Users/olegz/Documents/GitHub/StudyProj/lvl2/lesson1/ball.png', 0.1)
        self.ball.center_x = 300
        self.ball.center_y = 300


        
    def on_draw(self):
        #self.background_color = (255, 0, 0)
        self.clear((255, 255, 255))
        self.ball.draw()





window = Game(600, 600, "Ping Pong")













arcade.run()











