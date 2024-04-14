'''
Hierarchical Inheritance: 
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.
'''
'''Problem: 
If I want to access child1 property in child2 and print it, how i can do it ?
'''


class Parent:
    def __init__(self, property):
        self.property = property
    def show(self):
        print(f"{self.property}")

class child1(Parent):
    def __init__(self, property, name1):
        super().__init__(property)
        self.name1 = name1

    def showinfo(self):
        print(f"The {self.name1} have the {self.property}")

class child2(Parent):
    def __init__(self, property, name2):
        super().__init__(property)
        self.name2 = name2

    def showdetails(self):
        print(f"The {self.name2} have the {self.property}")
        # print(f"The property: {self.property}, \nchild1: {self.name1}, \nchild2: {self.name2}")


# a = child1("Shares", "Yogesh")
# a.showinfo()

# b = child2("Gold", "Rajesh", "Yogesh")
b = child2("Gold", "Rajesh")
b.showdetails()

