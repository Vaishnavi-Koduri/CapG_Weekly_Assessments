class Student:
    def __init__(self,name,roll_num,class_in):
        self.name= name
        self.roll_num= roll_num
        self.class_in= class_in

    def student_details(self,name,roll_num,class_in):
        print("Student details are as follows:")
        print(f"Student name: {self.name}")
        print(f"Student roll number: {self.roll_num}")
        print(f"Student is in {self.class_in}th class")

student = Student("Vaish",17,12)
student.student_details("Vaish",17,12)