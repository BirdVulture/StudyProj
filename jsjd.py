list = []
process = True
summ = 0
maxx = 0
minn = 1000


while process == True:
    money = int(input())
    list.append(money)
    if money == 0:
        process = False

for i in range(len(list)):
    
    if maxx < list[i]:
        maxx = list[i]

for i in range(len(list)):
    
    if minn > list[i] and list[i] != 0:
        minn = list[i]

summ = maxx - minn

print(list)
print(maxx)
print(minn)
print(summ)