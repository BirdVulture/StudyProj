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