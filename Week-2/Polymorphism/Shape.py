class shape:
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius= radius
    def area(self):
        return 3.14*self.radius**2

class square(shape):
    def __init__(self,side):
        self.side= side
    def area(self):
        return self.side**2

obj= circle(7)
obj2= square(3)
print(obj.area())
print(obj2.area())