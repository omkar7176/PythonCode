class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showdet(self):
        print(f"The employee name is {self.name} & her age is {self.age}")
class Programmer(employee):
    def __init__(self, name, age, comp, loc):
        super().__init__(name, age) 
        self.comp = comp
        self.loc = loc
    def showdetails(self):
        print(f"The Programmer name is {self.name} & her age is {self.age}. she works at the {self.loc} in the {self.comp} company.")

a = Programmer("Rutuja", 21, "Microsoft", "Pune")
b = Programmer("Omkar", 22, "Microsoft", "Pune")
a.showdetails()        
b.showdetails()        


