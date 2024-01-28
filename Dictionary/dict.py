                    # ** Dictionary in Python 
# A dictionary in Python is a data structure that stores the value in value:key pairs.
# Note: The dictionary do not allow duplicates.but it contain same key which represent the updated value.


Details = {'Name': "Omkar", 'City': "Pune", 'Comp': "Microsoft"}
info = {1 : "Ram", 2 : "Delhi", 3 : "Amazon"}
print(Details)
print(info)

# Creating the dictionary using function --> dict()
Student = dict(Name= "Omkar", Field= "Computer Science", Age= 22, Comp="Google")
print(Student)


# Accessing the Dictionary items

Pinfo = {'Name': "Shyam", 'City': "Kolkata", 'eligible': True}
# 1st way:
print(Pinfo.get('City'))
# OP: Kolkata

# 2nd Way but without get()
print(Pinfo['Name'])
# OP: Shyam





# Accessing the multiple values
print(Pinfo.values())
# OP: dict_values(['Shyam', 'Kolkata', True])





# Note: if the key is not presented in the dict & we print it the OP is None.
print(Pinfo.get('Color'))
# OP: None






# Accessing the keys:
print(Pinfo.keys())
# OP: dict_keys(['Name', 'City', 'eligible'])









# Accesing the key:values pair in single line.
print(Pinfo.items())
# OP: dict_items([('Name', 'Shyam'), ('City', 'Kolkata'), ('eligible', True)])






# Add items in Dictionary using update()
# 1st way:
emp = {'Name': "Shyam", 'Age' : 22, 'Company': 'Amazon', 'Year': 2024}
emp.update(Study="DSA")
print(emp)
#OP: {'Name': 'Shyam', 'Comp': 'Amazon', 'Age': 22, 'Year': 2024, 'Study': 'DSA'}



# 2nd way:
sample = {'Name': "Ram", 'Comp': "Google", 'Age' : 22, 'Year': 2023}
sample["Domain"] = "SDE"
print(sample)

# OP: {'Name': 'Ram', 'Comp': 'Google', 'Age': 22, 'Year': 2023, 'Domain': 'SDE'}





# Change the values in the dictionary.

country_info = {'IN': 'India', "CA": "England", "US": 'USA'}
country_info["CA"] = "Canada"
print(country_info)







# Adding elements to dictionary using different ways like using array indexing.
Language = {}
# print(Language)

Language[1]= "Python"
Language[2]= "Java"
Language[3]= "Javascript"
Language[4]= "Typescript"
print(Language)   # {1: 'Python', 2: 'Java', 3: 'Javascript', 4: 'Typescript'}
Language[4]= "C++"
print(Language) # {1: 'Python', 2: 'Java', 3: 'Javascript', 4: 'C++'}

#OP: That's the main difference







# Use Dictionary with the mixed keys and accesing the elements.
Dict  = {'Name': 'Rajesh', 'Numb': [1,2,3,4,5]}

print(Dict['Numb']) #--> OP: 'Numb': [1,2,3,4,5,6,7,8,9,0]

print(Dict)  #--> OP: {'Name': 'Rajesh', 'Numb': [1,2,3,4,5,6,7,8,9,0]}






# Different ways to create the dictionary in Python

info = {}

# using the dict() function
info = dict({1: 'Shreyash', 2: 22, 3: 'CS', 4: 'IIT Madras'})
print(info)
# OP: {1: 'Jayesh', 2: 22, 3: 'CS', 4: 'IIT Madras'}






# remove the element from the dict using  pop().
Student = {1 : "Omkar", 2: "Sanket", 3:"Kunal", 4: "Shreyash", 5: "John"}
Student.pop(5)
print(Student)
#OP: {1: 'Omkar', 2: 'Sanket', 3: 'Kunal', 4: 'Shreyash'}
candidate = Student.pop(5)
print(candidate)
#OP: John






# Deleting Elements using ‘del’ Keyword
Student = {1 : "Omkar", 2: "Sanket", 3:"Kunal", 4: "Shreyash", 5: "John"}
del(Student[5])
print(Student)
#OP: {1: 'Omkar', 2: 'Sanket', 3: 'Kunal', 4: 'Shreyash'}




#          **___Completed___**