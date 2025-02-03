class Electronics:
    def __init__(self, brand):
        self.brand = brand 

    def design(self):
        return f"{self.brand} has a state of the art design."
    
class MobileDevice(Electronics):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model 
    # Overriding the design method to add model information
    def design(self):
        # parent_message = super().design() 
        return f" The mobile device model {self.model} is now widely used."

# Derived class: SmartPhone, inherits from MobileDevice
class SmartPhone(MobileDevice):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os  
    def design(self):
        return f"{self.brand} {self.model} smartphone running {self.os} has a unique design."

    def app(self, app_name):
        return f"Using the {app_name} app on the {self.brand} {self.model} smartphone."

# Create an instance of SmartPhone and test the methods
phone = SmartPhone("Apple", "iPhone 15", "iOS")
print(phone.design())  
print(phone.app("Safari"))
phone1= MobileDevice("Samsung","S23")
print(phone1.design())
