class Employee:
    def __init__(self,name,id,department):
        self.name= name
        self.id= id
        self.department= department
    def display(self):
        print(f"Employee Name: {self.name}, Emplyee ID: {self.id}, Employee department: {self.department}")

employee= Employee("Vaish",101,"IT")
employee.display()
