#урок1


min = int(input())
max = int(input())


def count(n):
   global min

   #n - это номер слоя

   if n == min:

       return min

   else:
        x = count(n-1) + 1
        return x

#для 101 слоя вызов такой

print(count(max))



            
