"""
Day 43 - Encapsulation
Implement encapsulation in a class.
"""

class Parent:
    def __init__(self) -> None:
        self.a = "Hello"
        self._b = "World"
        self.__c = "!!!"

    def printC(self):
        print(self.__c)

print(Parent().a)
print(Parent()._b)

Parent().printC()

print(Parent().__c)