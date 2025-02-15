a = str(input())
b = a.split(" ")

def superman_int(x):        #функция для превращения списка строк в список чисел
    for i in range(len(x)):
        x[i] = int(x[i])
    return x

def superman_like7(x):
    count = 0
    for i in range(len(x)):
        if x[i] % 10 == 7:
            count += 1
    return count

print(superman_like7(superman_int(b)))

        