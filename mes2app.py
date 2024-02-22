import tkinter as tkn
from tkinter import ttk
import csv



'''mainWindow = tkn.Tk()
mainWindow.title("vulture_bird") #название
mainWindow.geometry("600x650")
mainWindow.minsize(600,650)   # минимальные размеры
mainWindow.maxsize(600,650)   # макисмальные размеры'''

contactsFileName = "ContactList.csv"
contacts = []

contactsData = ["мама", "сына", "мой номер"]
ServerLink = []



findedContactData = []

#Загрузка контактов
def LoadContactData(): 
    global contacts
    global contactsData
    with open(contactsFileName, "r", newline= "" ) as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row) 
            contactsData = contacts
        


LoadContactData()
print(contacts)
print(contactsData)             












#def sendMessageFunction():  

'''def findContactFunction(): # поиск контактов


    window = tkn.Tk()
    window.title("Add contact")
    window.geometry("250x150")
    window.minsize(250, 150)
    window.maxsize(250, 150)

    # поле для вывода результатов поиска
    label = ttk.Label(window, text="Результат поиска")
    label.pack(side="top", pady= 5)
    findedContact = tkn.Text(window, height= 2, width = 30)
    findedContact.pack(side="top", pady= 7)

    # кнопка добавления найденного контакта
    close_button = ttk.Button(window, text="Add contact", command=lambda: window.destroy())
    close_button.pack(side="bottom", pady= 5)

def connectFuction():
    window = tkn.Tk()
    window.title("Authorization")
    window.geometry("250x250")
    window.minsize(250, 250)
    window.maxsize(250, 250)

    # поле ввода ссылки подключения
    labelServerLink = ttk.Label(window, text="Connect Link")
    labelServerLink.pack(side="top", pady= 1)

    ServerLinkData = tkn.Entry(window, width = 20)
    ServerLinkData.pack(side="top", pady= 2)

    # поле ввода логина
    labelLogin = ttk.Label(window, text="Login")
    labelLogin.pack(side="top", pady= 3)

    login = tkn.Entry(window, width = 20)
    login.pack(side="top", pady= 4)

    # поле ввода пароля
    labelPass = ttk.Label(window, text="Password")
    labelPass.pack(side="top", pady= 5)

    password = tkn.Entry(window, width = 20)
    password.pack(side="top", pady= 6)


    #Кнопка подключения к серверу
    close_button = ttk.Button(window, text="Connect", command=lambda: window.destroy())
    close_button.pack(side="bottom", pady= 5)









#Сетка окна
for c in range(3): mainWindow.columnconfigure(index=c, weight=1)
for r in range(3): mainWindow.rowconfigure(index=r, weight=1)



#Buttons
sendButton = ttk.Button(text = "Send", width= 12) #Кнопка "Отправить"
sendButton.grid(row=3, column=3, ipadx=6, ipady=6, padx=5, pady=5)

findContactButton = ttk.Button(text = "Find contact", width= 12, command=findContactFunction) #Добавить контакт"
findContactButton.grid(row=0, column=1, ipadx=6, ipady=6, padx=2, pady=0)

connectButton = ttk.Button(text = "connect", width= 12, command=connectFuction) #подключение
connectButton.grid(row=0, column=3, ipadx=6, ipady=6, padx=5, pady=0)

#поле поиска контактов

messageField = tkn.Entry()
messageField.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)


#Поле сообщений
messagesField = tkn.Text(height= 40, width = 50)
messagesField.grid(row=2, column=1, columnspan=3, ipadx=6, ipady=6, padx=5, pady=5)

#Поле ввода (Text)
messageField = tkn.Text(height= 2, width = 55)
messageField.grid(row=3, column=0, columnspan=2, ipadx=6, ipady=6, padx=5, pady=5)
#скролл поля ввода
#scrollbar = ttk.Scrollbar(orient="vertical", command = messageField.yview)
#scrollbar.grid(row=3, column=2)
#messageField["yscrollcommand"]=scrollbar.set


#контакты (listbox)


contactsVar = tkn.Variable(value = contactsData)

contacts_listbox = tkn.Listbox(listvariable = contactsVar, height = 30, width = 20)
 
contacts_listbox.grid(row=2, column=0, ipadx=6, ipady=6, padx=5, pady=5)


mainWindow.mainloop()'''