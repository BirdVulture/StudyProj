
class Observed:
    def __init__(self):
        self.observer = Coordinator() #жестко закрепляем наблюдателя
        self.state = None
    

    #функция для передачи состояния наблюдателю
    def notifyObserver(self, state):
        self.observer.updateDataFromObserved(state)
        print("notify ok")

    #функция для изменения состояния и передачи его

    def setState(self, value):
        self.state = value
        self.notifyObserver(self.state)
        print("setState ok")
        




class Coordinator:

    #связь через свойства
    
    
    def __init__(self):
        self.executor = Executor()
        self.responseData = None
        self.stateObserved = None

    def callFunc(self):
        self.executor.printing()

    def takeAnswer(self):
        self.responseData = self.executor.classData
        print(self.responseData)


    #Функция, которую вызывает наблюдаемый при изменении состояния
    def updateDataFromObserved(self, state):
        
        self.stateObserved = state
        print(self.stateObserved)
        print("update ok")




class Executor:

    classData = "answer"

    def __init__(self):
        pass

    def printing(self):
        print("it's works")

    def doResponse(self):
        return self.classData



'''
testObject = Coordinator()

testObject.callFunc()
testObject.takeAnswer()
'''

testObject2 = Observed()

testObject2.setState("Data")







    
