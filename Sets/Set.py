#                                    ** Sets in Python
# A Set in Python programming is an unordered collection data type that is iterable, mutable 
# and has no duplicate elements. 
#  Set are represented by { } (values enclosed in curly braces).
# Sets are unordered
# Set elements are unque. Duplcate elements are not allowed in a set.







# * Sets in Python
# 1st way
x = {"Omkar", 234, True, False, ("Sanket")}
print(x)
# OP: {False, True, 'Sanket', 'Omkar', 234}
print(type(x))   # OP: <class 'set'>

# 2nd way
y = set()
print(y)
print("type of Y: ", type(y))







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