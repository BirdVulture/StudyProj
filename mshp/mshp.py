'''
a = str(input())
b = a.split(" ")

def superman_int(x):        #функция для превращения списка строк в список чисел
    for i in range(len(x)):
        x[i] = int(x[i])
    return x

def superman_like7(x):
    count = 0
    for i in range(len(x)):
        if x[i] % 10 == 7:
            count += 1
    return count

print(superman_like7(superman_int(b)))
'''

'''
a = list(map(int, input().split()))
for i in range(len(a)):
    print(f"{i}) {a[i]} проверен!")'
'''

a = list(map(int, input().split()))
index = []
def minimal_element(a):
    minimal = min(a)
    for i in range(len(a)):
        if a[i] == minimal:
            index.append(i)


def check_index(index):
    b = len(index)
    print("Индекс минимального элемента равен", index[b-1])



minimal_element(a)
check_index(index)

