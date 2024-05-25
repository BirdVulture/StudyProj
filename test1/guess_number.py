import random

def guess_number():

    print("Компьютер загадал число от 1 до 10. Попробуйте его угадать.")
    secret_number = random.randint(1, 10)
    attempts = 3
    while attempts > 0:
        print("Осталось попыток " + str(attempts))
        user_number = input("Введите число: ")
        user_number = int(user_number)
        if secret_number > user_number:
            print ("Секретное число больше")
        if secret_number < user_number:
            print ("Секретное число меньше")
        if secret_number == user_number: 
            print ("Вы угадали")
            break
        attempts = attempts - 1
    if attempts == 0:
        print("Вы проиграли") 
        print("Было загадно число: " + str(secret_number)) 

