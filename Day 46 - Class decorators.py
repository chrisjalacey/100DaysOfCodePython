"""
Day 46 - Class decorators
Use class decorators in Python.
"""

class Value:
    def __init__(self, savedValue) -> None:
        self._savedValue = savedValue

    lesson = "day 46 - class decorators"

    @property
    def savedValue(self):
        print("value")
        return self._savedValue
        

    @savedValue.setter
    def savedValue(self,inputValue):
        print("saved value set")
        if inputValue > 0:
            self._savedValue = inputValue - 1

    @savedValue.deleter
    def savedValue(self):
        print("saved value deleted")
        del self._savedValue

    @staticmethod
    #static method used when method is independant from a class instance
    def multiply(x,y):
        print("multiply x by y")
        return x * y
    
    
    @classmethod
    #Used for accessing class attributes
    def getLesson(cls):
        return cls.lesson
    
v = Value(5)
print(v.savedValue)
v.savedValue = 10
print(v.savedValue)

#del v.savedValue

print(v.multiply(1,2))
print(Value.getLesson())
