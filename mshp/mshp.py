#урок1

def num_digits(n):
    num = 0
    while n != 0:
        num %
        n //= 10
        num = num + 1
    return num
    
    
a = int(input())
b = num_digits(a)
print(b)