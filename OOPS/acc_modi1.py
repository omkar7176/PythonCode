'''
for protected = use '_' single underscore
1. Using the "protected" data members in other class using inheritance technique 
2. Using the "protected" data members in other class without inheritance technique in below 👇
3. Also we can access outside of the class.
'''

# 1.
class parent:
    def __init__(self , name, age):
        self._name = name
        self._age = age
    def show(self):
        print("Okay")

class child(parent):
    def __init__(self, _name, _age, loc):
        super().__init__(_name, _age)
        self.loc = loc
    def showdetails(self):
        print(f"Name: {self._name}  \nAge: {self._age} \nLocation: {self.loc}")    

a = child("Omkar", 21, "India")
a.showdetails()



'''2. Using the "protected" data members in other class without inheritance technique 👇'''

# 2.
class emp1:
    def __init__(self, name):
        self._name = name
    def show(self):
        print(f"Yess")
        
class emp2:
    def __init__(self, loc):
        self.loc = loc

    def showinfo(self):
        result = self.loc._name
        print(f"Accessing in child class: {result}")

a = emp1("Rutuja")
b = emp2(a)
b.showinfo()       



'''3. Also we can access outside of the class.'''
# 3

class information:
    _name = "Rutuja"
    _loc = "In my heart"
    _age = 21

a = information
print(a._name)
print(a._loc)
print(a._age)