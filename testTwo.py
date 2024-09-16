a = int(input())

min = a
max = a

while a != 0:
    if a < min:
        min = a
    if a > max:
        max = a
    a = int(input())
print (max)
print (min)    

