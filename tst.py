backpack = []
n = int(input())
for i in range(n):
    a = int(input())
    backpack.append(a)

print(backpack)

heavy = backpack[0]

for i in range(len(backpack)):
    if backpack[i] > heavy:
        heavy = backpack[i]

print(heavy)
        
        