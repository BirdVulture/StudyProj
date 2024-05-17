import psycopg

conn = psycopg.connect(dbname="littlebird1", user="user1", password="*******", host="79.174.88.184", port="17490")
cursor = conn.cursor()
''' 
# создаем таблицу people
cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
# поддверждаем транзакцию
conn.commit()
print("Таблица people успешно создана")

#
# добавляем строку в таблицу people
cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38)")
# выполняем транзакцию
conn.commit()  
print("Данные добавлены")

#
# данные для добавления
bob = ("Bob", 42)
cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", bob)
conn.commit()  
 
print("Данные добавлены")
#

# данные для добавления
people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", people)
 
conn.commit()  
print("Данные добавлены")

# получаем все данные из таблицы people
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())
'''





cursor.close()
conn.close()

