import tkinter as tk
from tkinter import *

HEIGHT = 2
WIDTH = 20
X = 350
Y = 50
CLR_BTN = "#DCDCDC"
CLR_WND = "#C0C0C0"
CLR_SRCH = "white"

window = tk.Tk()
window.geometry("600x600")
window.title("diaUP")

window["bg"] = CLR_WND

one_btn = tk.Button(text= "Найти продукт", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
two_btn = tk.Button(text= "Посмотреть продукт", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
three_btn = tk.Button(text = "Рассчитать", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
four_btn = tk.Button(text= "Поддержка", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
five_btn = tk.Button(text= "Выход", height= HEIGHT, width= WIDTH, bg = CLR_BTN)

#кнопки


one_btn.place (x = X, y = Y)
two_btn.place (x = X, y = Y * 2)
three_btn.place (x = X, y = Y * 3)
four_btn.place (x = X, y = Y * 4)
five_btn.place (x = X, y = Y * 5)

#поля ввода

search = tk.Entry(width= WIDTH, bg = CLR_SRCH)
search.place(x = 10, y = 50)

#поле для ввода кол-ва граммов
gramm = tk.Entry(width= WIDTH, bg = CLR_SRCH)
gramm.place(x = 10, y = 420)


#список продуктов

food_list = ["пицца", "пельмени"]
food_var = Variable(value=food_list)
food_listbox = Listbox(listvariable=food_var, width= WIDTH)
food_listbox.place(x = 10, y = 100)

#информация о продукте
info_block = tk.Text(height= 7, width= 25)
info_block.place(x = 10, y = 300)

#Лейблы

#one_label = tk.Label(window, text= "DiaUp", bg = "white")
#one_label.place (x = 190, y = 30)



window.mainloop()