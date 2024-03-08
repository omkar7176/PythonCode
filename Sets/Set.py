#                                    ** Sets in Python **
# A Set in Python programming is an unordered collection data type that is iterable, mutable 
# and has no duplicate elements. 
#  Set are represented by { } (values enclosed in curly braces).
# Sets are unordered
# Set elements are unque. Duplcate elements are not allowed in a set.
# What are sets --> ❌ (indexing, ordered, duplicate, mutable) ❌







# * Sets in Python
x ={}
print(x)
print(type(x))
# OP: {}
#     <class 'dict'>


fruits = {"apple", "orange", "banana", "cherry"}
print(fruits)
# OP: {'banana', 'cherry', 'apple', 'apple'}
print(type(fruits)) # OP: <class 'set'>


# 1st way
x = {"Omkar", 234, True, False, "Sanket"}
print(x)
# OP: {False, True, 'Sanket', 'Omkar', 234}
print(type(x))   # OP: <class 'set'>


# 2nd way
y = set()
print(y)
print("type of Y: ", type(y))
# OP: set()
#     type of Y:  <class 'set'>


# Set removes the duplicate values
a = {'a', 'b', 'c', 'a'}
print(a)
# OP: {'b', 'c', 'a'}






#get the length of set
a = {"Shyam", 21, 1000.0, True}
print(len(a))  #OP: 4





##the Set() constructor
set1 = set(("Ram", 21, 22))
print(set1)
print(type(set1))
# OP: {'Ram', 21, 22}
#     <class 'set'>




# Converting the list into Set --> need to create the new variable.

content = ["Omkar", "Shyam", "Ram", "Sanket", "Kunal", 2121, True]
info = set(content)
print(info)
# OP : {'Kunal', True, 2121, 'Sanket', 'Shyam', 'Omkar', 'Ram'}
print(type(info))    # OP: <class 'set'>





#without creating new variable.

Name = set(["Omkar", "Sanket", True, False, 32343.33, 32323])
print(Name)
print(type(Name))   # OP: <class 'set'>
# OP: {False, True, 32323, 'Omkar', 32343.33, 'Sanket'}







# Access the items in set using loop
setA = {"Om", "San", "jac", "dog", "cat", "mat"}
for i in setA:
    print(i)
# OP: Om
#   San
#   cat
#   mat
#   jac
#   dog
    



# check if items present in set or not using "in" operator 
fruits = {"Apple", "grapes", "cherry"}
print("Apple" in fruits)
# OP: True