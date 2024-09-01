n = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
backpack = [n, n1, n2, n3, n4, n5]
heavy = 0
for i in range(len(backpack)):
    if i > heavy:
        heavy = i
        print(heavy)
        