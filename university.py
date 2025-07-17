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
        
    def view_enrolled_courses(self):
        print(f"Current enrolled courses: {self.courses}")
        
    def view_gpa(self):
        print(f"GPA: {self.gpa}")
    
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
        print(f"""First Name:{self.first_name}
Last Name: {self.last_name}
Age: {self.age}
Email: {self.email}
Role: {self.role}
Student ID: {self.student_id}
GPA: {self.gpa}
Course: {self.courses}
            """)
        
# Professor class
class Professor(Person):
    def __init__(self, first_name, last_name, age, email, role, employee_id, department, courses):
        super().__init__(first_name, last_name, age, email, role)       
        self.employee_id = employee_id
        self.department = department
        self.courses = []                                   # empty list
        
    def assign_course(self, course):                            
        self.courses.append(course)                         # Adds to the list couress empty list
        print(f"Course Assign. {self.courses}")              # confirms it 
        
    def view_student_enrolled(self):
        student_enrolled = []
        for i in self.courses:
            student_enrolled.append(self.first_name)
            print(f"Student enrolled {self.first_name}")
    def display_info(self):
         print(f"""First Name:{self.first_name}
Last Name: {self.last_name}
Age: {self.age}
Email: {self.email}
Role: {self.role}
Employee ID: {self.employee_id}
Course: {self.courses}
Department{self.department}
            """)

# Admin class
class Admin(Person):
    def __init__(self, first_name, last_name, age, email, role, admin_id, premissions):
        super().__init__(first_name, last_name, age, email, role)
        self.admin_id = admin_id
        self.premissions = []
        
    def add_user(self):                                     # adds the user first name to the premissions[]
        if self.admin_id == "Abdulaziz":
            self.premissions.append(self.first_name)
            print("User added", self.premissions)
        else:
            print("Incorrect ID")
        
    def remove_user(self):                                   # removes the user first name to the premissions[]
        if self.admin_id == "Abdulaziz":
            self.premissions.remove(self.first_name)
            print("user removed", self.premissions)
        else:
            print("Incorrect ID")
            
    def display_info(self):
        print(f"""First Name:{self.first_name}
Last Name: {self.last_name}
Age: {self.age}
Email: {self.email}
Role: {self.role}
Admin ID: {self.admin_id}
Premissions: {self.premissions}
            """)
    
class Course():
    def __init__(self, course_code, course_name, enrolled_students):
        self.course_code = course_code
        self.course_name = course_name
        self.enrolled_students = []
        
    def add_student(self, student):                     # Adds student name to the enrolled_students []
        self.enrolled_students.append(student)
    
    def remove_student(self, student):                  # Removes student name from the enrolled_students []
        self.enrolled_students.remove(student)

    def display_course_info(self):                      # prints the information
        print(f"""Course Code:{self.course_code}
Course Name: {self.course_name}
Enrolled Students: {self.enrolled_students}
              """)
