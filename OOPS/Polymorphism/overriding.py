'''Method Overriding:
- Method overriding in Python refers to the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass (parent class).
- same function name in parent class and child class, & access the property from the parent class. 
'''

# Example 1
class parent:
    def showinfo(self, name):
        self.name = name
    def show(self):
        print(f"{self.name}")
class child(parent):
    def showinfo(self, name, age):
        super().showinfo(name)
        self.age = age
        print(f"The name is {self.name} and age is {self.age}.") 
obj = child()
obj.showinfo("Omkar", 21)     

# Example 2

class Employee:
   def __init__(self,name, sal):
      self.name=name
      self.sal=sal
   def getName(self):
      return self.name
   def getsal(self):
      return self.sal

class office(Employee):
   def __init__(self,name, sal, incnt):
      super().__init__(name,sal)
      self.incnt = incnt
   def getsal(self):
      print(f"Name: {self.name} \nSalary: {self.sal} \nIncentive: {self.incnt}")

a = office("Raj", "50,000", 2000)
a.getsal()      

