
# Example 3:
class parent:
    def __init__(self, name):
        self.name = name

    def display_parent(self):
        print(f"Parent's name: {self.name}")

class child(parent):
    def __init__(self, name, age):
        super().__init__(name) # Call parent class constructor
        self.age = age

    def display_child(self):
        print(f"Child's name: {self.name} & his age is {self.age} years old.")

child_obj = child("Shon", 4)
child_obj.display_child()        