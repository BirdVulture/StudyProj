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

def hello(to):
    print("hello, ", to)  
    




def main():
    hello()
    name = input("What is your name? ")
    hello(name)


def mainTwo()
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n): #степнь n ** 2
    return pow(n, 2)

