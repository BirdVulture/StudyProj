

class Coordinator:
    executor = ()
    responseData = ()
    
    def __init__(self):
        self.executor = Executor()

    def callFunc(self):
        self.executor.printing()

    def takeAnswer(self):
        self.responseData = self.executor.classData
        print(self.responseData)

class Executor:

    classData = "answer"

    def __init__(self):
        pass

    def printing(self):
        print("it's works")

    def doResponse(self):
        return self.classData




testObject = Coordinator()

testObject.callFunc()
testObject.takeAnswer()
    
