"""
Day 39 - Class Object
Create a class for a simple car with methods like start and stop.
"""

class Car:
    def __init__(self, colour) -> None:
        self.colour = colour

    def start(self):
        print(f"The {self.colour} car is started")

    def stop(self):
        print(f"The {self.colour} car is stopped")


c = Car("red")
c.start()
c.stop()