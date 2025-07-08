""" 
This project is about University system using OOP concept 
"""
class University:
    def __init__(self, name):
        self.name = name
        
    # geter and seters
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def __str__(self):
        return f"The University Name is: {self.name}"

        
    