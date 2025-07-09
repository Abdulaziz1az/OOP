""" 
This project is about University system using OOP concept 
"""
from abc import ABC, abstractclassmethod
class Person(ABC):
    def __init__(self, first_name, last_name, age, email, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.role = role
        
        
    def display_info(self):
        pass
    
class Student(Person):
    def __init__(self, student_id, gpa, courses):
        self.student_id = student_id
        self.gpa = gpa
        self.courses = []
        
    def enrole(self, course):
        self.courses.append(course)
        print("course enroled")
    
    def calculate_gpa(self):
        pass
    
    def display_info(self):
        pass
        
        
        

        
    