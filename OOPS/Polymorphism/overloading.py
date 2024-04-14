'''Method Overloading:
- Same function name but different parameters in same class.
- When you have a class with the method of one name defined more than once but with different argument types and/or return types, it is a case of method overloading.
'''


# Example 1
class alpha:
    def show(self, a, b):
        print("A and B: ", a, b)
    def show(self, c, d):
        print("C and D: ", c, d)
obj = alpha()
obj.show(10, 20)        
obj.show(50, 40)       

# Example 2
class student:
    def info(self, name=''):
        print("The name is", name)
obj = student()
obj.info() # same function works as twice this is called method overloading.
obj.info("Omkar") # same function works as twice this is called method overloading.


# Example 3
class glass:
    def product(self, a, b, d):
        p = a * b * d
        print("The multiplication : ", p)
    def product(self, ac, bc, dc):
        ab = ac+bc+dc
        print("The addition : ",ab)
obj = glass()
obj.product(2, 5, 10)


# Example 4
class student:
    def book(self, name, price):
        print("The book name and price: ", name, price)
    def book(self, date):
        print("date: ", date)
obj = student()
obj.book("The autobiography of Yogi")        

# Example 5
'''Problem: how we can access the "name" from the teacher'''
class teacher:
    def show(self, name):
        print("Name of author: ", name)
    def show(self, price):
        print("Price of book: ", price)
class student:
    def show(self, date):
        print("Publish date: ", date)
    def show(self, copies):
        print("Number of copies: ", copies)
a = teacher()
a.show("Omkar")     
a.show(500)    