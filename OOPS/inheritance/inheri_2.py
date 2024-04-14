
''' Inheritance *
When access the property from parent class & child class also have own property, how we can access the parent property ?
 '''

# Example 1:

class Parent:
    def __init__(self, Id, name):
        self.Id = Id
        self.name = name

    def showemp(self):
        print(f"The ID {self.Id} is a {self.name}")

class Child(Parent):
    def __init__(self, Id, name, occ, comp):
        super().__init__(Id, name) # Call parent class constructor
        self.occ = occ
        self.comp = comp

    def showdeatis(self):
        print(f"The ID: {self.Id} is a {self.name} & occ is {self.occ} at {self.comp}.")

child_obj = Child(1, "Omkar", "DevRel", "Microsoft")
child_obj.showdeatis()