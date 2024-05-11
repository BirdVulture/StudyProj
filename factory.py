import time


class Store:
    def __init__(self, n):
        self.balance = n

    def input(self):
        self.balance += 1

    def output(self):
        if self.balance > 0:
            self.balance -= 1
            out = 1
        else:
            out = 0
                  
        return out
    
    def show_balance(self):
        return self.balance
    
    
        


class Machine:
    def __init__(self, productivity ):
        self.productivity = productivity


    def readiness(self): #Счетчик готовности продукции
        self.ready = 0
        while self.ready < 10:
            print(self.ready)
            time.sleep(0.1)
            self.ready += 1
            
        return self.ready   
    
    def production(self): #Производство, работает пока на складе сырья остаток больше 0. Готовая продукция складывается на склад готовой продукции
        self.raw = store_one.output()
        
        if self.raw > 0:
            print ("Вход на станок", self.raw)
            self.complete = self.readiness()
            print(self.complete)
            if self.complete == 10:
                store_two.input()
                print("Остаток на складе сырья", store_one.show_balance())
                print("Остаток на складе продукции", store_two.show_balance())
                self.production()

        



    
store_one = Store(int(input("Введите количество сырья "))) #Склад готовой продукции
print("Остаток на складе", store_one.balance)

machine_one = Machine(2) #станок

store_two = Store(0) #Склад готовой продукции


machine_one.production()
