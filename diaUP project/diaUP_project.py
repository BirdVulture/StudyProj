import tkinter as tk


HEIGHT = 2
WIDTH = 30
X = 350
Y = 50
CLR_BTN = "#DCDCDC"
CLR_WND = "#C0C0C0"
CLR_SRCH = "white"

window = tk.Tk()
window["bg"] = CLR_WND
window.geometry("600x600")
window.title("diaUP")



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

search = tk.Entry(width= WIDTH, bg = CLR_SRCH)
search.place(x = 10, y = Y)

#список продуктов

food_list = ["пицца", "пельмени"]
food_var = tk.Variable(value=food_list)
food_listbox = tk.Listbox(listvariable=food_var, width= WIDTH)
food_listbox.place(x = 10, y = Y * 2)


#Лейблы

#one_label = tk.Label(window, text= "DiaUp", bg = "white")
#one_label.place (x = 190, y = 30)



window.mainloop()