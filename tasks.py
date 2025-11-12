class StringSource:
    def __init__(self, strings):
        self.strings = strings
        
    def get_length(self,):
        return len(strings)   
        
class ListSource:
    def __init__(self, lists):
        self.lists = lists
        
    def get_length(self,):
        return len(lists)
        
def print_source_length(source):
    return f"Длина источника: {source.get_length}"

lists = ListSource([1, 2, 3])



list1234 = [1, 2, 3]
print(list1234)

