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
        return True
    else:
        return False
    


    