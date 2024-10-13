#урок1

def deposit(x, a, n):
    summ = x
    for i in range(n):
        summ = summ + (summ * a / 100)
    
    return summ



x, a, n = list(map(int, input().split()))
print("{:.4f}".format(deposit(x, a, n)))
            
