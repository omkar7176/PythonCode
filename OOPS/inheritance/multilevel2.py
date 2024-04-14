# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"{self.name} age: {self.age}")

# Intermediate Class
class Employee(Person):
    def __init__(self,name, emp_id, dept):
        Person.__init__(self, name, age=30)
        self.emp_id = emp_id
        self.dept = dept
    def showinfo(self):
        print(f"ID no {self.emp_id} and Dept: {self.dept}")

# Derived Class
class Manager(Employee):
    def __init__(self, name, reports):
        Employee.__init__(self, name, emp_id=12, dept="comp")
        self.reports = reports
    def showdetails(self):
        print(f"Person name: {self.name}, \nAge:{self.age}, \nID: {self.emp_id}, \nDept: {self.dept}, \nReport: {self.reports}")
a = Manager("Omkar", "Good") 
a.showdetails()       
