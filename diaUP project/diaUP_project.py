#я как пользователь хочу используя приложение посчитать количество хлебных единиц и поставить нужное количество инсульна
#я как пользователь хочу найти в поиске нужный мне продукт для того, чтобы понять сколько в нем углеводов
#нужно выбрать продукт в списке
#нужно ввести его название в поле ""

import tkinter as tk
from tkinter import *

HEIGHT = 2
WIDTH = 30
X = 350
Y = 50
CLR_BTN = "#DCDCDC"
CLR_WND = "#C0C0C0"

window = tk.Tk()
window.geometry("600x600")
window.title("diaUP")

window["bg"] = CLR_WND

one_btn = tk.Button(text= "Найти продукт", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
two_btn = tk.Button(text= "Добавить свой продукт в список", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
three_btn = tk.Button(text = "Приступить к расчету", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
four_btn = tk.Button(text= "Поддержка", height= HEIGHT, width= WIDTH, bg = CLR_BTN)
five_btn = tk.Button(text= "Выход", height= HEIGHT, width= WIDTH, bg = CLR_BTN)

#кнопки


one_btn.place (x = X, y = Y)
two_btn.place (x = X, y = Y * 2)
three_btn.place (x = X, y = Y * 3)
four_btn.place (x = X, y = Y * 4)
five_btn.place (x = X, y = Y * 5)

#поля ввода

search = tk.Entry(width= WIDTH)
search.place(x = 10, y = 50)

#список продуктов

food_list = ["пицца", "пельмени"]
food_var = Variable(value=food_list)
food_listbox = Listbox(listvariable=food_var, width= WIDTH)
food_listbox.place(x = 10, y = 100)
#Лейблы

#one_label = tk.Label(window, text= "DiaUp", bg = "white")
#one_label.place (x = 190, y = 30)



window.mainloop()