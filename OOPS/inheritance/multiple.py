'''Multiple Inheritance :
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. 
In multiple inheritances, all the features of the base classes are inherited into the derived class. 
'''

class emp1: # base class 1
    def fun1(self, name):
        self.name = name
    def fun2(self):
        print("Okay")   
class emp2: # base class 2
    def fun3(self, loc):
        self.loc = loc
    def fun4(self):
        print("Yess")
class emp3(emp1, emp2): # child class
    def fun5(self):
        print(f"{self.name} and {self.loc}")
        
a = emp3()
a.name = "Rutuja"
a.loc = "In_meh_heart"
a.fun5()        