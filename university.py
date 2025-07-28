""" 
This project is about University system using OOP concept 
"""
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, first_name, last_name, age, email, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.role = role
    @abstractmethod   
    def display_info(self):
        pass
    def get_full_name(self):
        return f"{self.role.capitalize()}: {self.first_name} {self.last_name}"
    
class Student(Person):
    def __init__(self, first_name, last_name, age, email, role, student_id, gpa, courses):
        super().__init__(first_name, last_name, age, email, role)
        self.student_id = student_id
        self.gpa = gpa
        self.courses = {}
        
    def enroll(self, course):
        if course not in self.courses:
            self.courses[course] = None
            print(f"{course} Successfully enrolled!")
        else:
            print(f"{course} is alread enrolled!")
    
    def update_grade(self, course, grade):
        if course in self.courses:
            self.courses[course] = grade
            print(f"Grade updated: {course} -> {grade}")
        else:
            print(f"{course} is not enrooled yet")
    def view_enrolled_courses(self):
        print("Enrolled Course:")
        for course, grade in self.courses.items():
            grade_display = grade
            if grade:
                grade_display = grade
            else:
                print("Not graded")
            print(f"- {course}: {grade_display}")
    
    def calculate_gpa(self):
        points = {"A": 4, "B": 3, "C":2, "D":1, "F": 0}
        total = 0
        count = 0
        for course, grade in self.courses.items():
            if grade is None:
                continue
            if  grade in points:
                total += points[grade]
                count += 1
            
        if count > 0:
            avg = total / count
            self.gpa = round(avg, 2)
            print(f"GPA calculated: {self.gpa}")
        else:
            print("No grades available to calculate GPA.")
    
    def view_gpa(self):
        if self.gpa is not None:
            print(f"GPA: {self.gpa}")
        else:
            print("GPA has not been calculated yet.")
    

        print(self.get_full_name)

    def display_info(self):
        print(f"""First Name:{self.get_full_name()}
Age: {self.age}
Email: {self.email}
Role: {self.role}
Student ID: {self.student_id}
GPA: {self.gpa}
Course: {self.courses}
            """)
        
# Professor class
class Professor(Person):
    def __init__(self, first_name, last_name, age, email, role, employee_id, department):
        super().__init__(first_name, last_name, age, email, role)       
        self.employee_id = employee_id
        self.department = department
        self.courses = []
        
    def assign_course(self, course):                            
        if course not in self.courses:
            self.courses.append(course)
            print(f"{course.course_code} - {course.course_name} Successfully assigned.")
        else:
            print(f"{course} is alread assigned.")
        
    def view_assigned_courses(self):
        if not self.courses:
            print("No courses assigned yet.")
        else:
            for course in self.courses:
                print(f"Assigned Courses:{course.course_name}")
            
    
    def view_students_in_courses(self):
        if not self.courses:
            print("No courses assigned yet.")
        else:
            for course in self.courses:
                print(f"\nCourse: {course.course_name}") 
                if not course.enrolled_students:
                    print(" No student enrolled.")
                else:
                    for student in course.enrolled_students:
                        print(f"  -{student.get_full_name()}")   
    def display_info(self):
        Course_list = [course.course_name for course in self.courses]
        print(f"""First Name:{self.first_name}
Last Name: {self.last_name}
Age: {self.age}
Email: {self.email}
Role: {self.role}
Employee ID: {self.employee_id}
Course: {', '.join(Course_list) if Course_list else 'None'}
Department{self.department}
            """)

# Admin class
class Admin(Person):
    def __init__(self, first_name, last_name, age, email, role, admin_id):
        super().__init__(first_name, last_name, age, email, role)
        self.admin_id = admin_id
        self.premissions = ["add_user", "remove_user", "view_all"]
        
    def add_user(self, user, user_registry):                                     # adds the user first name to the premissions[]
        if self.admin_id in self.premissions:
            user_registry.append(user)
            print(f"User added: {user.get_full_name()}")
        else:
            print("Permission denied.")
        
    def remove_user(self, user, user_registry):                                   # removes the user first name to the premissions[]
        if "remove_user" in self.premissions:
            if user in user_registry:
                user_registry.remove(user)
                print(f"User removed: {user.get_full_name()}")
        else:
            print("Permission denied.")
    def view_all_courses_people(self, user_registry):
         print("Users and their courses:")
         for user in user_registry:
             print(user.get_full_name())
             if hasattr(user, "courses"):
                 if isinstance(user.courses, dict):
                     for course, grade in user.courses.items():
                         print(f"- {course.course_name if hasattr (course, 'course_name') else course}")
            
    def display_info(self):
        print(f"""Admin info:
Name:{self.first_name} {self.last_name}
Age: {self.age}
Email: {self.email}
Role: {self.role}
Admin ID: {self.admin_id}
Premissions: {self.premissions}
            """)
    
class Course():
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = None
        self.enrolled_students = []
        
    def add_student(self, student):                     # Adds student name to the enrolled_students []
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"{Student.get_full_name()} enrolled in {self.course_code}.")
        else:
            print(f"{Student.get_full_name()} is alread enrolled.")
    
    def remove_student(self, student):                  # Removes student name from the enrolled_students []
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"{Student.get_full_name()} removed from {self.course_code}.")
        else:
            print(f"{Student.get_full_name()} is not enrroled in {self.course_code}")
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

    def display_course_info(self):                      # prints the information
        print(f"\nCourse Info:")
        print(f"Code: {self.course_code}")
        print(f"Name: {self.course_name}")
        print(f"Instructor: {self.instructo.get_full_name()if self.instructor else 'Not assigned'}")
        print("Enrolled Students:")
        if not self.enrolled_students:
            print(" None")
        else:
            for student in self.enrolled_students:
                print(f"  - { Student.get_full_name()}")

p1 = Professor("Az", "Am", 22, "ad@gmail.com", "Prof", "akdj2", "MATH")
math_c = Course("MAth", "M")
p1.assign_course(math_c)
c1 = Course("CS50","Intor to programing")
p1.assign_course(c1)
