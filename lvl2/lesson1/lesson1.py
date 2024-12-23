#https://drive.google.com/drive/folders/1v1f0UO200TmzRXMd1YczYwYjEROIn1Vk?usp=drive_link
#pip install arcade
#https://pypi.org
#https://api.arcade.academy/en/latest/api/window.html#arcade.Window
#https://api.arcade.academy/en/latest/arcade.color.html
#command= для привязки функции к кнопке
#https://www.youtube.com/watch?v=4GYCAl_wpx0
#https://tproger.ru/news/--entuziast-sozdal-igru-na-chistom-assemblere-bez-ispolzovaniya-bibliotek
import arcade
import arcade.key


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TITLE = "Пинг понг"
CHANGE_X = 6
CHANGE_Y = 6


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
        #print("enter in update bar")
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0
         

class Game(arcade.Window):
    def __init__ (self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('/Users/olegz/Documents/StudyProj/lvl2/lesson1/ball.png', 0.1)
        self.bar = Bar('/Users/olegz/Documents/StudyProj/lvl2/lesson1/bar.png', 0.1)
        self.setup()
        self.score = 0
        self.attempts = 3
        self.game = True
    def setup(self):
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.ball.change_x = CHANGE_X
        self.ball.change_y = CHANGE_Y
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = 0
        

    def on_draw(self):
        self.clear((255, 255, 255))
        self.ball.draw()
        self.bar.draw()
        arcade.draw_text(f"Счет: {self.score}", 20, SCREEN_HEIGHT - 30, (0,0,0), 20)
        arcade.draw_text(f"Попытки: {self.attempts}", 20, SCREEN_HEIGHT - 70, (0,0,0), 20)
        if self.attempts == 0:
            arcade.draw_text("GAME OVER", SCREEN_HEIGHT / 6, SCREEN_WIDTH / 2, (255, 33, 33), 50)
            self.game = False
        if self.score == 20:
            arcade.draw_text("YOU WIN", SCREEN_HEIGHT / 6, SCREEN_WIDTH / 2, (255, 33, 33), 50)
            self.game = False


    #def on_key_press(self, key, modifiers):
    def on_key_press(self, symbol: int, modifiers: int):
        if self.game == True:
            if symbol == arcade.key.A:
                self.bar.change_x = -CHANGE_X
            if symbol == arcade.key.D:
                self.bar.change_x = CHANGE_X
            print(arcade.key.LEFT)   
        

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.bar.change_x = 0



        #print("enter in pn key press")
        #блок для стрелочек


        '''
        if symbol == arcade.key.LEFT:
            self.bar.change_x = -CHANGE_X
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = CHANGE_X
        '''
        
         

    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.ball, self.bar) == True:
            self.ball.bottom = self.bar.top
            self.ball.change_y = self.ball.change_y * (-1)
            self.score = self.score + 1
        if self.ball.bottom <= 0:
            self.setup()
            self.attempts = self.attempts - 1
            print("work")
        if self.attempts == 0:
            self.ball.stop()
            self.bar.stop()  
        if self.game == False:
            self.ball.stop()
            self.bar.stop()


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)













arcade.run()






'''
дз
написать консольное приложение в диапозоне от 0 до 100, чтобы оно ходило с определенным шагом бесконечно в диапозоне от 0 до 100

'''




#ошибка в том, что ( change_x = -4 )




