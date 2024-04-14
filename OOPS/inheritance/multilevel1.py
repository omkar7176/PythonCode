'''
Multilevel Inheritance:
- In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather. '''
class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food  = food
    def show(self):
        print(f"{self.name}, {self.food}")
class Dog(Animal):
    def __init__(self, name, sound):
        Animal.__init__(self, name, food="chicken")
        self.sound = sound
    def show_info(self):
        print(f"{self.sound}")
class rocky(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, sound="bark")
        self.color = color
    def show_details(self):
        print(f"Dog name: {self.name}, \nSound: {self.sound}, \nColor: {self.color}, \nFood: {self.food}")
a = rocky("Ronny", "White-blue")
a.name = "Monty"
a.show_details()