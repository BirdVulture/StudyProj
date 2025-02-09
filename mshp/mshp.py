a = input()
b = a.split(" ")

def superman_int(x):        #функция для превращения списка строк в список чисел
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def superman_remove2(x):    #функция для удаления двоек
    x.remove(2)
    return x


def superman_average(x):
    if len(x) == 0:
        print("К сожалению, у вас были только двойки")
    else:
        summ = 0
        for i in range(len(x)):
            summ = summ + x[i]
        aver = summ / len(b)
        print(round(aver, 2))


c = superman_int(b)
d = superman_remove2(c)
print(c)
print(d)
#superman_average(d)
