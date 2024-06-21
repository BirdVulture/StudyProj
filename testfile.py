import psycopg

conn = psycopg.connect(dbname="littlebird1", user="user1", password="!Yh506Qpjm@", host="79.174.88.184", port="17490")
cursor = conn.cursor()

cursor.execute("SELECT * FROM people")
for person in cursor.fetchall():
    print(f"{person[1]} - {person[2]}")


cursor.close()
conn.close()