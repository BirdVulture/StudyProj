'''
import csv 
with open("favorites.csv", "r") as file:
    #1 reader = csv.reader(file)
    reader = csv.DictReader(file)
    scratch = 0
    c = 0
    python = 0

    scratch, c, python = 0, 0, 0 #1


    #1
    for row in reader:
        #1 print(row[1])
        #1 favorite = row[1]
        favorite = row["language"] # for Dict
        print(favorite) #1
        print(row["language"]) #2
    #2
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c +=1
        elif favorite == "Python":
            python +=1

print(f"Scratch:{scratch}")
print(f"C:{c}")
print(f"Python:{python}")

#counters clever sample
with open("favorites.csv", "r") as file:
    
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite =  row["language"]
        if favorite in counts:
            counts[favorite]  += 1
        else:
            counts[favorite] = 1

for favorite in sorted(counts, key=counts.get, reverse=True): 
    print(f"{favorite}: {counts[favorite]}")

##
import csv
from collections import Counter

with open("favorites.csv", "r") as file:
    
    reader = csv.DictReader(file)
    counts = Counter()
    for row in reader:
        favorite = row["problem"] #may "language change to "problem"
        counts[favorite] += 1

#1
for favorite in sorted(counts, key=counts.get, reverse=True): 
    print(f"{favorite}: {counts[favorite]}")

#2
for favorite, count in counts.most_common():
     print(f"{favorite}: {count}")

'''
'''
##!!!! input and count 
import csv
from collections import Counter

with open("favorites.csv", "r") as file:
    
    reader = csv.DictReader(file)
    counts = Counter()

    for row in reader:
        favorite = row["problem"] #may "language change to "problem"
        counts[favorite] += 1

favorite = input("Favorite: ")
print(f"{favorite}: {counts[favorite]}")
'''

#sqlite3 //terminal command HEADER

#sqlite3 favorites.db //create a new DB
#.mode csv 
#.import favorites.csv favorites
#.schema //table format
#SELECT * FROM favorites;
#SELECT language FROM favorites;
#SELECT language FROM favorites LIMIT 10; //only 10 values
#SELECT COUNT(*) FROM favorites; // count number of rows
#SELECT DISTINCT(language) FROM favorites; //return unique values from colomn
#SELECT COUNT(DISTINCT(language)) FROM favorites; //return number of unique values from colomn
#SELECT COUNT(*) FROM favorites WHERE language = 'C';
#SELECT COUNT(*) FROM favorites WHERE language = 'C'AND problem = 'C';
#SELECT language, COUNT(*) FROM favorites GROUP BY language;
#SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);
#SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) ASC; //from smollest to biggest
#SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC; // from biggest to smollest
#SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC; //time 51:50
#blueprint# INSERT INTO table (colomn, ...) VALUES (value, ...);
#INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');
#DELETE FROM favorites WHERE Timestamp IS NULL;
#blueprint#  UPDATE table SET colomn = value WHERE condition;
#DELETE FROM favorites; // delete all data
#UPDATE favorites SET problem = 'TEST' WHERE language = 'C';


#sqlite3 shows.db
#SELECT * FROM shows
#CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, year NUMERIC, episodes INTEGER, PRIMARY KEY(Id)) 
#INSERT INTO shows (id, title, year, episodes) VALUES ('62614','Zeg ns Aaa ', '1981', '227')

#BLOB //Binary large object
# INTEGER
#NUMERIC
#REAL
#TEXT
#NOT NULL UNIQUE
#PRIMARY KEY is ID
#FOREIGN KEY

#