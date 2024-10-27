#урок1
import random

def throw_green_dice():
    #бросок зеленого кубика
    x = random.randint(1, 6)
    answer = 0
    if x == 1 or x == 2 or x == 3:
        answer = 1
        print("преступник сдался")
    elif x == 4 or x == 5:
        answer = 0
        print("преступник сбежал")
    elif x == 6:
        answer = 1000
        print("прогремел выстрел")

    return answer

#throw_green_dice()

def pick_dice(broski):
    green = broski // 10
    red =  broski % 10
    n = green + red
    y = random.randint(1, n)
    if 1 <= y <= green:
        print("вытащили зелёный!")
    else:
        print("вытащили красный")
pick_dice(49)



