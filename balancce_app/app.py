from tkinter import *
from tkinter import ttk
 
window = Tk()
window.title("My Balance")
window.geometry("600x650")
window.minsize(600,650)   # минимальные размеры
window.maxsize(600,650)   # макисмальные размеры'''


#Кнопки
btn_income = Button(text="Приход") # создаем кнопку из пакета tkinter
btn_income.place(x=20, y=120)    # размещаем кнопку в окне

btn_outcome = Button(text="Расход") # создаем кнопку из пакета tkinter
btn_outcome.place(x=120, y=120)    # размещаем кнопку в окне

#поле ввода
input_data = Entry(text="Приход")
input_data.place(x=20, y=20, width= 200)

 
window.mainloop()
