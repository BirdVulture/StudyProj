#https://drive.google.com/drive/folders/1v1f0UO200TmzRXMd1YczYwYjEROIn1Vk?usp=drive_link
#pip install arcade
#https://pypi.org
#https://api.arcade.academy/en/latest/api/window.html#arcade.Window
#https://api.arcade.academy/en/latest/arcade.color.html
import arcade 

class Ball(arcade.Sprite):
        def update(self):
            self.center_x += self.change_x
            #self.center_y += self.change_y
            if self.right >= 600:
                self.change_x = -self.change_x
            elif self.left <= 0:
                self.change_x = -self.change_x




            '''    
            if self.bottom <= 0:
                self.change_y = -self.change_y
            elif self.top >= 600:
                self.change_y = -self.change_y
           '''
            

class Game(arcade.Window):
    def __init__ (self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('/Users/olegz/Documents/GitHub/StudyProj/lvl2/lesson1/ball.png', 0.1)
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 100
        self.ball.change_y = 5
    def update(self, delta_time):
         self.ball.update()
         

        
    def on_draw(self):
        #self.background_color = (255, 0, 0)
        self.clear((255, 255, 255))
        self.ball.draw()





window = Game(600, 600, "Ping Pong")













arcade.run()











