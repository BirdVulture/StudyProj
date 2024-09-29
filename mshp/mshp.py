#урок1



list = []
for i in range(5):
    a = float(input())
    b = round(a)
    if (a - b) >= 0.5:
        b = b + 1
    list.append(b)
print(list)
for i in range(len(list)):
    print(list[i])
