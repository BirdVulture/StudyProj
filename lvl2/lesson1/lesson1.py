#https://drive.google.com/drive/folders/1v1f0UO200TmzRXMd1YczYwYjEROIn1Vk?usp=drive_link
#pip install arcade
#https://pypi.org

import arcade 

class Game(arcade.Window):
    def __init__ (self, width, height, title):
        super().__init__(width, height, title)
    def on_draw(self):
        #self.background_color = (255, 0, 0)
        self.clear((255, 0, 0))

window = Game(500, 600, "Ping Pong")













arcade.run()











