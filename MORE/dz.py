#Папа

flag = "y"

coord = 0
change = 10

while flag == "y":
    
    coord = coord + change
    print(coord)
    flag = str(input("продолжать? y/n "))

    if coord >= 100 or coord <= 0:
        change = - change

