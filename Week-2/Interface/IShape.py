# Create an interface `IShape` with an abstract method `calculate_area()`. 
# Implement it in `Rectangle` and `Circle` classes.

from abc import ABC, abstractmethod

class iShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(iShape):
    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth
    def calculate_area(self):
        return self.length*self.breadth

class Circle(iShape):
    def __init__(self,radius):
        self.radius= radius
    def calculate_area(self):
        return 3.14*self.radius**2
    
obj= Rectangle(5,10)
print(obj.calculate_area())
obj1= Circle(3)
print(obj1.calculate_area())

