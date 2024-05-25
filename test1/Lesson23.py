#https://www.youtube.com/@eleday https://ru.stackoverflow.com/questions/872005/%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5-%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%B2

'''
import lesson1_1 as file1
import guess_number as file2

def menu():
    print("1 игра поле чудес: ")
    print("2 Игра угадай число: ")
    print("3 выйти: ")

while True:
    print("Привет! Во что ты хочешь поиграть?")
    menu()
    value = int(input("Во что вы хотите поиграть?"))
    if value == 1:
        file1.pole_chudes()
        print("Вы закончили играть")
    elif value == 2:
        file2.guess_number()
    else:
        break
#file1.pole_chudes()
'''