#Documentation
#https://docs.python.org/3.12/library/index.html
  
#STR
# Ask user for their name
'''name = input("What is your name?")

#remove whitespace from str
name = name.strip()

#Capitalize name 
name = name.capitalize()

#Title
name = name.title()

#Split user's name into  first name and last name (to split strings by separator)
first, last = name.split(" ")
 
print(f"Hello, {name}")

print(first,"\n" ,last, sep= "--", end= "\n")

print(first + last)'''

#INTEGER 1:04
'''
x = int(input("What's x? "))
y = int(input("What's y?"))

z = x + y

print(z)
'''
#FLOAT 1:19
'''
x = float(input("What's x? "))
y = float(input("What's y?"))

z = x + y

print(z)
 
#round (округление)

z = round(x + y)

z = round(x / y, 2) #round

print(z)

'''
#FUNCTIONS (def) 1:31
'''
def hello(to):
    print("hello, ", to)  
    

hello()


def main():
    hello()
    name = input("What is your name? ")
    hello(name)


def mainTwo():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n): #степнь n ** 2
    return pow(n, 2)
'''

# Conditionals (условия) 1:50
'''
xy = int(input("What's x? "))
 = int(input("What's y?"))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal than y")


if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal than y")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal than y")   
'''
    
'''
score = int(input("Score: "))

if score >= 90 and score <=100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: D")

# This code is better
if 90 <= score <=100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: D")

# This code is more better
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: D")
'''
# Parity
'''
x = int(input("What's x? "))
y = int(input("What's y?"))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# Even or odd (четное/нечетное) 
def is_even(n):
    if n % 2 ==0:
#        return True
#    else:
#        return False


# the better code
        
          
def is_even_two(n):
    return True if n % 2 == 0 else False



# The more better code
def is_even(n):
    return n % 2 == 0
'''    

#match
'''
name = input("What's your name? ")

if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Ron":
    print("Griffendor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who")
'''
# Another way (Соответствие)
'''
match name:
    case "Harry":
        print("Griffendor")
    case "Hermione":
        print("Griffendor")
    case "Ron":
        print("Griffenor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# the better code 
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffendor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

'''
#Loops 2:46
'''        
i = 3

while i != 0: # while  i is not equal 0 
    print("meow")
    i = i - 1
'''
'''
for i  in [0, 1, 2]:
    print("meow")

#the better code
for i in range(3):
    print("meow")

#the more better code
print("meow\n" * 3, end="")

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break 
'''
'''
#the better code (через функции)

def main():
    number = get_number()
    meow(number)

while True:
    n = int(input("What's n? "))
    if n > 0:
        break 

for i in range(n):
    print("meow")

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
        return n

def meow(n):
    for _ in range(n):
        print("meow")



main()
'''

# list 3:21
'''
students = ["Hermione", "Harry", "Ron"]
'''
 
#for each element in list
''' 
for student in students:
    print(student)
'''

'''
for i  in  range(len(students)):
    print(i + 1, students[i])
'''
    



# dicts 3:32
'''
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Griffindor", "Griffindor", "Griffindor", "Slytherin"]
'''
'''
students = {
    "Hermione": "Griffidor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}


print(students["Hermione"])
print(students["Harry"])
print(students["ron"])
print(students["Draco"])


for student in students:
    print(student, students[student], sep= ", ")
'''
'''
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
'''
'''
def main():
    print_column(3)
'''
'''
def print_column(height):
    for _ in range(height):
        print("#")
'''
# more clever code
'''
def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
     print("?" * width)

def print_square(size):

    #for each row in square 
    for i in range(size):

        #for efch brich in row
        for j in range(size):

            #print brick
            print("#", end="")

        print()     
'''
#another way
'''
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(widht):
    print("#" * widht)

main()
'''

#Exceptions 4:15 (обработка ошибок ( если введен неверный тип данных))
'''
def main():
    x = get_int()
    print(f" x i {x}")


def get_int():
    while True: #запрашивать x пока ч не станет равно int
        try:
            x = int(input("What's x?"))       
            print(f"x is {x}")

        except ValueError:
            print("x is not an integer")

        else:
            return x


# the better code
        
def get_int():
    while True: #запрашивать x пока ч не станет равно int
        try:
           return int(input("What's x?"))       
           
        except ValueError:
            print("x is not an integer")

#another way without  error message
            
def get_int(prompt):
    while True: #запрашивать x пока ч не станет равно int
        try:
           return int(input(prompt))       
           
        except ValueError:
            pass #цикл без сообщеия об ошибке 


main()
'''
#Libraries 4.54
#module random
'''
import random

coin = random.choice(["heads", "tails"])


from random import choice

coin = choice(["heads", "tails"]) 
print(coin)

number = random.randint(1, 10)
print (number)

cards = ["jack", "queen", "king"]
random.shuffle(cards) #перемешать порядок элементов из списка
for card in cards:
    print(card)




#statistics
    
import statistics

print(statistics.mean([100, 90]))


#5.13 module sys

import sys

print("hello, my name is ", sys.argv[0]) #from filename

try: 
    print("hello, my name is ", sys.argv[0])

except IndexError:
    print("hello, my name is ", sys.argv[0])

#

if len(sys.argv) < 2:

    print("Too few arguments")

elif len(sys.argv) > 2:
    print("Too many arguments")

else:
     print("hello, my name is ", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

else:
    print("hello, my name is ", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is ", arg)


#Slices 5:32

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is ", arg)  

#PIP - package manager pypi.org
#python3 -m pip install "module name"
'''

#APIes pypi.org 5:47

#JSON 5:48
'''
import json
import requests
import sys

#if len(sys.argv) != 2:
#    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + "weezer")

#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
'''
# Libraries 6:02 
#Export and import functions from another file

#sayngs.py file with functions
'''
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

main()
'''
#another file
'''
import sys

from sayings import goodbye

if len((sys.argv)) == 2:
    goodbye(sys.argv[1])
'''
    
#Unit Tests 6:09

#program Calculator
'''
def main ():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

if __name__ == "__main__":
    main()
# test program
    

def main():
    test_square()

from calculator import square

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squred was not 9")


if __name__ == "__main__":
    main()
'''
#assert 6:20
'''
def main():
    test_square()

from calculator import square

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")    


if __name__ == "__main__":
    main()
'''
#pytest 6:25

#pyton3 pip inastall pytest
'''
from calculator import square
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0
'''
# run pytest!!!
'''
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
'''
#program
'''
def main():
    name = input("What's your name?")
    hello(name)

def hello(to="world"):
    print("hello,", to)

if __name__ == "__name__":
    main()
'''
# test program
'''
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

def test_argument2():
    for name in ["Hermione", "Harry"]:
        assert hello(name) == f"hello, {name}"

#packages
'''

#File I/O 7:00 
#LIST
'''
names = []

for _ in range(3):
    name = input("What's your name?")
    names.append(name)


print(f"hello, {name}")

#clever code

names = []

for _ in range(3):
    names.append(input("What's your name?"))


print(f"hello, {name}")
'''
#create file
'''
name = input("What's your name?")

file = open("names.txt", "w")
file.write(name)
file.close()

#clever code
name = input("What's your name?")

file = open("names.txt", "w")
file.write(f"{name}\n")
file.close()

#with
# add data to file
name = input("What's your name?")

with open("names.txt", "a") as file: # "a" - add data to file
    file.write(f"{name}\n") # add data to new line in file

#read lines from file and write it to list

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip()) #rstrip remove white spaces

#more compact code

with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())

names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

#more compact code

with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello, ", line.rstrip()) 
'''

#csv file
# Export from .csv, split each line for two elements by ,
'''
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''

#Dictionaries! key-value

'''
students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


#sort dictionaries
    
students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


#with lambda function

students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key=lambda student: student[name]):
    print(f"{student['name']} is in {student['house']}")


#csv library
    
import csv

students = []
with open ("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})


#back the dictionary 

import csv

students = []
with open ("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

#8:14

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

#

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


#Images
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
'''

# REGULAR EXPRESSIONS 8:30
