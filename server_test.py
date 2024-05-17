import psycopg

conn = psycopg.connect(dbname="littlebird1", user="user1", password="*****", host="79.174.88.184", port="17490")
print("Подключение установлено")
conn.close()

