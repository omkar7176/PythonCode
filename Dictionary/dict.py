                            #   ** Dictionary in Python 
"""
# 1. A dictionary in Python is a data structure that stores the value in value:key pairs.
# 2. Note: The dictionary do not allow duplicates. but it contain same key which represent the updated value.
# 3. What are the dictionary --> ❌(indexing, duplicate) and  ✔(Ordered, Mutable)
# 4. "Values" in a dictionary can be of any data type and can be duplicated, whereas "keys" can’t be repeated and must be immutable. 
# 5. Note - Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. """




''' Dictionary Syntax:
# var = {key1 : value1, key2 : value2, ......}
'''

# Create the empty dictionary
empty_var = {}
print("Empty_Dictionary: ", empty_var)
print(type(empty_var))
# OP: {}
#    <class 'dict'>









# Create the dict with different data types of elements.
student = {
    'Name': "Shyam",
    'Country': "India", 
    'Age': 21, 
    'Working': True, 
    'CGPA': 8.85
    }
print("Elements in dictionary: ",student)
print(type(student))
# OP: Elements in dictionary:  {'Name': 'Shyam', 'Country': 'India', 'Age': 21, 'Working': True, 'CGPA': 8.85}
#     <class 'dict'>





# Different ways to create the Dictionary

# Example 1
# A dictionary can also be created by the built-in function dict().
var1 = dict({
    'Name': 'Ram', 
    'Age': 22
    })
print(var1)
print(type(var1))
# OP: {'Name': 'Ram', 'Age': 22}
#     <class 'dict'>


# Example 2
var2 = dict([
    (1, 'Omkar'), 
    (2, 'Ram'), 
    (3, 'Shyam')
    ])
print(var2)
print(type(var2))
# OP: {1: 'Omkar', 2: 'Ram', 3: 'Shyam'}
#     <class 'dict'>









# Add the elements in empty dictionary.

# Example 1:
a = {}
print("Empty Dictionary: ",a)
a[1] = "Hello, "
a[0] = "Good Morning"
a[2] = "Everyone"
a[0] = "Good Afternoon" #Always print the updated value
a['values'] = 5678
print("After the adding elements: ", a)
# OP: Empty Dictionary:  {}
#     After the adding elements:  {1: 'Hello, ', 0: 'Good Afternoon', 2: 'Everyone', 'values': 5678}





# Example 2:
sample = {
    'Name': "Ram", 
    'Comp': "Google", 
    'Age' : 22, 
    'Year': 2023
    }
sample["Domain"] = "SDE"
print(sample)
# OP: {'Name': 'Ram', 'Comp': 'Google', 'Age': 22, 'Year': 2023, 'Domain': 'SDE'}






# Example 3:
Language = {}
print(Language)

Language[1]= "Python"
Language[2]= "Java"
Language[3]= "Javascript"
Language[4]= "Typescript"
print(Language)   # {1: 'Python', 2: 'Java', 3: 'Javascript', 4: 'Typescript'}
Language[4]= "C++"
print(Language) # {1: 'Python', 2: 'Java', 3: 'Javascript', 4: 'C++'}
#OP: That's the main difference






# Accesing the elements from dictionary

# Example 1:
candidate = {
    "Name" : "Ram", 
    'Country': "India", 
    'Age': 21, 
    'Working': True, 
    'CGPA': 8.85
    }
print(candidate['Country'])
# OP: India



# Example 2:
color = {
    1:'White', 
    2:'Red', 
    3:'Green', 
    4:'blue', 
    5: 'Yellow'
    }
print(color)
print(type(color))
print(color[5])
# OP: {1: 'White', 2: 'Red', 3: 'Green', 4: 'blue', 5: 'Yellow'}
#     <class 'dict'>
#     Yellow








# Accessing an Element of a Nested Dictionary

alphabet = {1:{'IND': "India"}, 
            4:{'UK': "United Kingdom"},
            2:{'Ger': 'Germany'},
            3:{'USA': 'United State of America'}
            }
print(alphabet[4]['UK'])
print(alphabet[1])
# OP: United Kingdom
#    {'IND': 'India'}







# Change the values in the dictionary.

country_info = {
    'IN': "India", 
    'CA': "England", 
    'AUS': "Australia"
    }
country_info["CA"] = "Canada"
print(country_info)
# OP: {'IN': 'India', 'CA': 'Canada', 'AUS': 'Australia'}




'''___Completed___'''
# Recently Done