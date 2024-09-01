#https://www.psycopg.org
#pip install --upgrade pip           # upgrade pip to at least 20.3
#pip install "psycopg[binary]"       # remove [binary] for PyPy


import psycopg

conn = psycopg.connect(dbname="littlebird1", user="user1", password="*******", host="79.174.88.184", port="17490")
cursor = conn.cursor()
'''
# СОЗДАНИЕ ТАБЛИЦЫ
# создаем таблицу people
cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
# поддверждаем транзакцию
conn.commit()
print("Таблица people успешно создана")

#CREATE
# добавляем строку в таблицу people
cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38)")
# выполняем транзакцию
conn.commit()  
print("Данные добавлены")

# вставка кортежа
bob = ("Bob", 42)
cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", bob)
conn.commit()  
 
print("Данные добавлены")

# вставка списка кортежей
people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", people)
 
conn.commit()  
print("Данные добавлены")

#READ
# получаем все данные из таблицы people
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())

#вывод списка кортежей построчно- таблица
cursor.execute("SELECT * FROM people")
for person in cursor.fetchall():
    print(f"{person[1]} - {person[2]}")


cursor.execute("SELECT * FROM people")
# извлекаем первые 3 строки в полученном наборе
print(cursor.fetchmany(3))  # [(1, 'Tom', 38), (2, 'Bob', 42), (3, 'Sam', 28)]
# извлекаем следующие 3 строки в полученном наборе
print(cursor.fetchmany(3))  # [(4, 'Alice', 33), (5, 'Kate', 25)]

cursor.execute("SELECT * FROM people")
# извлекаем одну строку
print(cursor.fetchone())    # (1, 'Tom', 38)

cursor.execute("SELECT name, age FROM people WHERE id=2")
# раскладываем кортеж на две переменных
name, age = cursor.fetchone()
print(f"Name: {name}    Age: {age}")    # Name: Bob   Age: 42


#UPDATE
# обновляем строки, где name = Tom
cursor.execute("UPDATE people SET name ='Tomas' WHERE name='Tom'")
# вариант с параметрами
# cursor.execute("UPDATE people SET name =%s WHERE name=%s", ("Tomas", "Tom"))
conn.commit()
 
# проверяем 
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())    # [(2, 'Bob', 42), (3, 'Sam', 28), (4, 'Alice', 33), (5, 'Kate', 25), (1, 'Tomas', 38)]


# данные для множественного добавления
people = [(15, "Sam"), (18, "Alice")]
cursor.executemany("UPDATE people SET age =%s WHERE name=%s", people)
conn.commit()
 
# проверяем 
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())    # [(2, 'Bob', 42), (5, 'Kate', 25), (1, 'Tomas', 38), (3, 'Sam', 15), (4, 'Alice', 18)]

#DELETE
# обновляем строки, где name = Tom
cursor.execute("DELETE FROM people WHERE name=%s", ("Bob",))
conn.commit()
 
# проверяем 
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())    # [(5, 'Kate', 25), (1, 'Tomas', 38), (3, 'Sam', 15), (4, 'Alice', 18)]

# удаляем строки с id =3 и id=5
people = [(3,), (5,)]
cursor.executemany("DELETE FROM people WHERE id=%s", people)
conn.commit()
 
# проверяем 
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())    # [(1, 'Tomas', 38), (4, 'Alice', 33)]

'''
cursor.close()
conn.close()

