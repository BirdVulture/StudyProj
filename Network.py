#А - целочисленный массив  с индексами от 0 до 5
A = [3, 1, 2, 2, 0, 1]

rez = A[0]

for i in range(1, len(A)):
    if rez < A[i] :
        rez = A[i]
print(rez)
