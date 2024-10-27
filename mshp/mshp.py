#урок1

min = int(input())
max = int(input())

def rec(max):
    global min
    x = max
    if x != min:
        rec(max - 1)
    print(x)
 
    
rec(max)
            
