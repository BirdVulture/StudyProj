def func():
    print("ok")

if __name__ == "__main__":
    func()
else:
    print("вы подключили файл как не основной")
    print(__name__)