from abc import ABC, abstractmethod

# Abstract class
class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass

# Concrete class implementing ICalculator
class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

calc = BasicCalculator()
print(calc.add(5, 3))         
print(calc.subtract(5, 3))    
print(calc.multiply(5, 3))    
print(calc.divide(5, 0))      
