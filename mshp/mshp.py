import re
def removeHTML(text):
    return re.sub(r'\<[^>]*\>', '', text)
from urllib import request

# подключаемся к странице в Интернете и выкачиваем её код себе в программу:
connect = request.urlopen("https://www.cbr.ru/key-indicators/")
text = connect.read().decode()

# зацепка в html коде, которая указывает, где начинается информация про евро:
what = 'Евро'

# ищем, с какого по индексу символа начинается эта старт-зацепка:
start = text.find(what)

# зацепка в html коде, которая указывает, где заканчивается информация про евро:
end = text.find("евро", start+len(what))

# Вырезаем кусочек кода с начальной ко конечную зацепки и убираем лишний html код вокруг числа (курса евро):
text1 = text[start:end]
print("Курс ЕВРО =", removeHTML(text1))