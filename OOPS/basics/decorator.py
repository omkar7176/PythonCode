'''NOTE: 
if you add "@greet" before the function hello, then just call the function like "hello()".
BUT
if you not add "@greet" before the function hello, then call function like "greet(hello)()".
'''


# Example 1: Without argument in hello() function
def greet(argue):
    def modify_func():
        print("Good Morning")
        argue()
        print("Thanks For Using the func")
    return modify_func

@greet
def hello():
    print("HELLO EVERYONE")

def book():
    print("The Autobiography of Yogi")    

hello()    
greet(book)()



# Example 2:

def greet1(argue):
    def modify_func(*args, **kwargs):
        print("Morning Sir")
        argue(*args, **kwargs)
        print("Thank you sir")
    return modify_func


def add(a, b):
    print(a*b)    


greet1(add)(5, 3)
# add(10, 5)
