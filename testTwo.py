"""
class Calculator:
    num1 = 0
    num2 = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition (self, num1, num2):
        sum = num1 + num2
        return sum
    def subtraction (self, num1, num2):
        sum = num1 - num2
        return sum


c  = Calculator(0, 0)

a= int(input())
b= int(input())


print(c.addition(a, b))
print(c.subtraction(a, b))
"""

class Coin:
    #x = int
    #y = int

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y


coin = Coin("изображение", 100, 320)
coin2 = Coin("изображение", 200, 320)


print(coin.x)
print(coin.y)



#screen.blit(coin.image, (coin.x, coin.y)