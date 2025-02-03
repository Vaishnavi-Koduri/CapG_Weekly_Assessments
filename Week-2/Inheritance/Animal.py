class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Dogs bark if they feel threatened"

class Cat(Animal):
    def speak(self):
        super().speak()
        return "Cats scratch if they feel threatened"
    
dog= Dog()
print(dog.speak())
cat = Cat()
print(cat.speak())