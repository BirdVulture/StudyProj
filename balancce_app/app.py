import tkinter as tk
from tkinter import ttk

 
window = tk.Tk()
window.title("My Balance")
window.geometry("600x650")
window.minsize(600,650)   # минимальные размеры
window.maxsize(600,650)   # макисмальные размеры'''
bg = "#C0C0C0"

#Кнопки
btn_income = tk.Button(text="Приход") # создаем кнопку из пакета tkinter
btn_income.place(x=20, y=120)    # размещаем кнопку в окне

btn_outcome = tk.Button(text="Расход") # создаем кнопку из пакета tkinter
btn_outcome.place(x=120, y=120)    # размещаем кнопку в окне

#поле ввода
input_data = tk.Entry(text="Приход", background = bg)
input_data.place(x=20, y=20, width= 20)

 
window.mainloop()
