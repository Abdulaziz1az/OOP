""" 
This project is about University system using OOP concept 
"""
class Person():
    def __init__(self, first_name, last_name, age, email, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.role = role
        
        
    def display_info(self):
        print("info")
    
class Student(Person):
    def __init__(self, first_name, last_name, age, email, role, student_id, gpa, courses):
        super().__init__(first_name, last_name, age, email, role)
        self.student_id = student_id
        self.gpa = gpa
        self.courses = []
        
    def enrole(self, course):
        self.courses.append(course)
        print("course enroled")
    
    def calculate_gpa(self):
        if self.gpa == "A":
            print("4")
        elif self.gpa == "B":
            print("3")
        elif self.gpa == "C":
            print("2")
        elif self.gpa == "D":
            print("1")
        elif self.gpa == "F":
            print("0")
        else:
            print("invalid") 

    def display_info(self):
        print(f" First Name:{self.first_name}\n Last Name: {self.last_name}\n Age: {self.age}\n Eamil: {self.email}\n Role: {self.role}\n Student ID: {self.student_id}\n GPA: {self.gpa}\n Course: {self.courses}".format())
        
# Professor class
class Professor(Person):
    def __init__(self, first_name, last_name, age, email, role, employee_id, department courses):
        super().__init__(first_name, last_name, age, email, role)       
        self.employee_id = employee_id
        self.department = department
        self.courses = []                                  # empty list
        
    def assign_course(self, course):                            
        self.courses.append(course)                         # Adds to the list couress empty list
        print("Course Assign.")                             # confirms it 
    
    def display_info(self):
        print(f" First Name:{self.first_name}\n Last Name: {self.last_name}\n Age: {self.age}\n Eamil: {self.email}\n Role: {self.role}\n Employee ID: {self.employee_id}\n Course: {self.courses}\n Department{self.department}".format())
        