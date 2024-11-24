

def replace_name():
    #имя
    w = str(input())
    #строка
    w1 = str(input())
    if w1.find(w) == True:
        w1 = w1.replace(w, "[username]")
    print(w1)

replace_name()



