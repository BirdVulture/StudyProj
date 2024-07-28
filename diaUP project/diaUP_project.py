#я как пользователь хочу используя приложение посчитать количество хлебных единиц и поставить нужное количество инсульна
#я как пользователь хочу найти в поиске нужный мне продукт для того, чтобы понять сколько в нем углеводов
#нужно выбрать продукт в списке
#нужно ввести его название в поле ""

import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("diaUP")
one_btn = tk.Button(text= "Открыть список продуктов", height= 17, width= 25, bg = "gray")
two_btn = tk.Button(text= "Добавить свой продукт в список", height= 17, width= 25)
three_btn = tk.Button(text = "Приступить к расчету", height= 17, width= 25)
four_btn = tk.Button(text= "Поддержка", height= 17, width= 25)
five_btn = tk.Button(text= "Выход", height= 17, width= 25)

#кнопки


one_btn.place (x = 190, y = 50)
two_btn.place (x = 190, y = 80)
three_btn.place (x = 190, y = 110)
four_btn.place (x = 190, y = 140)
five_btn.place (x = 190, y = 220)


#Лейблы

one_label = tk.Label(window, text= "DiaUp", bg = "white")
one_label.place (x = 190, y = 30)



window.mainloop()