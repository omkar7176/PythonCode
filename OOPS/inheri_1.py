''' Inheritance *
Just use the property from parent class and access in child class'''

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showemp(self):
        print(f"The Employee is: {self.id} is {self.name}")

class Programmer(Employee):
    def showdetails(self):
        print(f"The Programmer from child access the parent property - {self.name} & ID: {self.id}")

e1 = Employee("Rutu", 26)
e1.showemp() 
e2 = Programmer("Omkar", 44)
e2.showdetails()
