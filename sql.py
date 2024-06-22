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

#sqlite3 //terminal command
#sqlite3 favorites.db create a new DB
#.mode csv 
#.import favorites.csv favorites