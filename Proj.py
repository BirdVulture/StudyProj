import tkinter as tk

def winner():
    #По горизонтали X
    if area[0][0]["text"] == "X" and area[0][1]["text"] == "X" and area[0][2]["text"] == "X":
        return "X"
    elif area[1][0]["text"] == "X" and area[1][1]["text"] == "X" and area[1][2]["text"] == "X":
        return "X"
    elif area[2][0]["text"] == "X" and area[2][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    

    #По диагонали X
    if area[0][0]["text"] == "X" and area[1][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    elif area[0][2]["text"] == "X" and area[1][1]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    
    #По вертикали X
    if area[0][0]["text"] == "X" and area[1][0]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    elif area[0][1]["text"] == "X" and area[1][1]["text"] == "X" and area[2][1]["text"] == "X":
        return "X"
    elif area[0][2]["text"] == "X" and area[1][2]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    
    
    #По горизонтали 0
    if area[0][0]["text"] == "0" and area[0][1]["text"] == "0" and area[0][2]["text"] == "0":
        return "0"
    elif area[1][0]["text"] == "0" and area[1][1]["text"] == "0" and area[1][2]["text"] == "0":
        return "0"
    elif area[2][0]["text"] == "0" and area[2][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    
    #По диагонали 0
    if area[0][0]["text"] == "0" and area[1][1]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    elif area[0][2]["text"] == "0" and area[1][1]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    
    #По вертикали 0
    if area[0][0]["text"] == "0" and area[1][0]["text"] == "0" and area[2][0]["text"] == "0":
        return "0"
    elif area[0][1]["text"] == "0" and area[1][1]["text"] == "0" and area[2][1]["text"] == "0":
        return "0"
    elif area[0][2]["text"] == "0" and area[1][2]["text"] == "0" and area[2][2]["text"] == "0":
        return "0"
    return ("")


def push(but):
    global turn
    print(turn)
    if (turn % 2) == 0:
        turn_char = "0" 
    else:
        turn_char = "X"
    print (f"Совершают ход: {turn_char}")
    if but ["text"] is "":
        but["text"] = turn_char
        turn = turn + 1
        if winner() == "x":
            print("Победили крестики!")
        if winner() == "0":
            print("победили нолики:")
        if winner() == "":
            print("Ничья!")
    #turn += 1 


window = tk.Tk()
window.title("Крестики нолики")
window.geometry("300x300")
window.resizable(False, False)
area = []
turn = 1
#print(push())

for x in range (3):
    area.append([])
    for y in range (3):
        button = tk.Button(window, text = "", width= 13, height = 6)
        area[x].append(button)
        area[x][y].place(x = x * 100, y = y * 100)
        area[x][y]["command"] = lambda selected_button = button: push(selected_button)




print(area)


window.mainloop()
