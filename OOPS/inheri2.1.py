
# Example 2:
class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showemp(self):
        print(f"The emp {self.name} have ID NO. {self.id}")
class Programmer(employee):
    def __init__(self,name, id, occ, loc):
        super().__init__(name, id) # Call the parent class constructor
        self.occ = occ
        self.loc = loc

    def showdeatils(self):
        print(f"Id no. {self.id} is {self.name} and she is {self.occ} work at {self.loc}.")
        

        

child_obj = Programmer("Rutu", 44, "SDE", "Pune")
child_obj.showdeatils()