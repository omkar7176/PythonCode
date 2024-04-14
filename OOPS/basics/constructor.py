class employee:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"The {self.name} is a {self.occ}.")

a = employee("Ram", "Full Stack Developer")
b =  employee("Omkar", "DevOps Engineer")# "self" is argument is automatically assign for the object a.


a.info()         
b.info()



''' Types of Constructor 

1. Parametrized Constructor
- When the constructor accepts argument along with "self", is known as Parametrized constructor.
ex. def __init__(self, name, occ):

2. Default  Constructor
- When constructor does not accept any argument from object & has only one argument "self" in constructor, is known as default constructor.
ex. def __init__(self):

'''