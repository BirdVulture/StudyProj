#урок1

def months(x, favorite_month):
    num = x // 10000 % 100
    answer = ""
    if num == favorite_month:
        answer = "Да"
    else:
        answer = "Нет"
    return answer
    
favorite_month = int(input())
data = int(input())
answer = months(data, favorite_month)
print(answer)