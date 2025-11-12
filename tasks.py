class StringSource:
    def __init__(self, strings):
        self.strings = strings
        
    def get_length(self):
        return len(self.strings)
        
        

class ListSource:
    def __init__(self, lists):
        self.lists = lists
    
    def get_length(self):
        return len(self.lists)
    

source = StringSource("abcd")

print (f"Длина источника: {source.get_length()}")