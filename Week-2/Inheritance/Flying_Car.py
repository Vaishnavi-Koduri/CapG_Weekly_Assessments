class Car:
    def road(self):
        return "Cars move on the ground!"

class Airplane:
    def sky(self):
        return "Airplanes fly in the sky"

class FlyingCar(Car,Airplane):
    pass
    def move(self):
        return "Flying Cars can both fly in the sky and move on the ground"
    
flyingcar= FlyingCar()
print(flyingcar.road())
print(flyingcar.sky())
print(flyingcar.move())