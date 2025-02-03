class Vehicle:
    def start(self):
        pass
    def stop(self):
        pass
 
class Car(Vehicle):
    def __init__(self,speed):
        self.speed= speed
    def start(self):
        if self.speed>0:
            return "The Car starts to move"
        else:
            return "Increase your speed to start the Car"
    def stop(self):
        if self.speed == 0:
            return "The Car is already stopped."
        else:
            self.speed = 0
            return "The Car stops moving."
    
class Bike(Vehicle):
    def __init__(self,speed):
        self.speed= speed
    def start(self):
        if self.speed>0:
            return "The Bike starts to move"
        else:
            return "Increase your speed to start the Bike"
    def stop(self):
        if self.speed == 0:
            return "The Bike is already stopped."
        else:
            self.speed = 0
            return "The Bike stops moving."

class ElectricCar(Car):
    def __init__(self,speed):
        self.speed= speed
    def start(self):
        if self.speed>0:
            return "The ElectricCar starts to move"
        else:
            return "Increase your speed to start the ElectricCar"
    def stop(self):
        if self.speed == 0:
            return "The ElectricCar is already stopped."
        else:
            self.speed = 0
            return "The ElectricCar stops moving."

car = Car(8)
print(car.start()) 
print(car.stop())   
print(car.stop())   

bike = Bike(12)
print(bike.start())  
print(bike.stop()) 
print(bike.stop())   

electricCar = ElectricCar(0)
print(electricCar.start())  
print(electricCar.stop()) 