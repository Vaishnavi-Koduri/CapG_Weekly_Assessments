class Employee:
    def role1(self):
        return "The employee's role is to complete the tasks given by the Manager"

class Manager:
    def role2(self):
        return "The Manager manages and takes care of his/her employees"
    def approve_leave(self):
        return "Your leave is approved"

class Person(Employee,Manager):
    pass
    def work(self):
        return "Both Employee and Manager work everyday"
    
person= Person()
print(person.role1())
print(person.role2())
print(person.approve_leave())
print(person.work())
