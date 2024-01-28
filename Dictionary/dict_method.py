# Dict Methods: 

# 1. clear() : It removes all the items in the dictionary and returns an empty dictionary.

dict_sample = {'Name': 'Shyam', 'Comp': 'Google', 'Field': 'Computer Science', 'Age': 22}
dict_sample.clear()
print(dict_sample)
# OP : {}




#2.copy(): It returns a shallow copy of the main dictionary

dict_sample = {'Name': 'Ajay', 'Comp': 'Google', 'Field': 'Computer Science', 'Age': 22}
sample = dict_sample.copy()
print(sample)
print(dict_sample)

# OP : {'Name': 'Ajay', 'Comp': 'Google', 'Field': 'Computer Science', 'Age': 22}
#      {'Name': 'Ajay', 'Comp': 'Google', 'Field': 'Computer Science', 'Age': 22}




# 3.items(): It returns a list of key:value pairs in a dictionary. The elements in the lists are tuples.

Student = {"Name": "Omkar", "Age": 22, "Field":"Computer Science", "Location": "Delhi"}
Student.items()
Student ['Location'] = "Pune"
print(Student)
# OP : {'Name': 'Omkar', 'Age': 22, 'Field': 'Computer Science', 'Location': 'Pune'}






# 4. keys(): to get the keys in the dictionary.
# There is need to create the new variable.

info = {"Name": "Omkar", "Age": 22, "Field":"Computer Science", "Location": "Delhi"}
candidate = info.keys()
print(candidate)
# OP: dict_keys(['Name', 'Age', 'Field', 'Location'])






# 5. values(): to get the values in the dictionary.
# There is need to create the new variable.

info = {"Name": "Omkar", "Age": 22, "Field":"Computer Science", "Location": "Delhi"}
candidate = info.values()
print(candidate)
# OP : dict_values(['Omkar', 22, 'Computer Science', 'Delhi'])






# 6. popitem(): It s used to remove the abitrary items from the dictionary and returns as a tuple.
            # In popitem(), no parameter values
            # popitem(), it just removes the last key pair in the dictionary.

info = {"Name": "Omkar", "Age": 22, "Field":"Computer Science", "Location": "Delhi"}
info.popitem()
print(info)
# OP: {'Name': 'Omkar', 'Age': 22, 'Field': 'Computer Science'}






# 7. pop(): This function is used to remove a "specific item" from the dictionary.
        # pop(), mention parameter values()
        # If we don't provide any value it will remove the last inserted data.

info = {"Name": "Omkar", "Age": 22, "Field":"Computer Science", "Location": "Delhi"}
info.pop('Age')
print(info)
# OP: {'Name': 'Omkar', 'Field': 'Computer Science', 'Location': 'Delhi'}






# 8. update() : to add the new element in the existing dictionary, also we can concatente the 2 dictionary using update().
topic = {'Name': 'Kunal', "College": 'BITS', "Location": "Mumbai"}
topic.update(Study="DSA")
print(topic)
#OP: {'Name': 'Kunal', 'College': 'BITS', 'Comp': 'Google', 'Location': 'Mumbai', 'Study': 'DSA'}

# concat the 2 dictionary
Student = {'Name': "Shyam",'Year': 2024}
topic.update(Student)
print(topic)
# OP: {'Name': 'Shyam', 'College': 'BITS', 'Location': 'Mumbai', 'Year': 2024}







# 9. get(): it returns the value of specified key if the present in dictionary otherwise return as none.
color = {1: "White", 2: "Yellow", 3: "black", 4: "Red"}

print(color.get(1))  # 1st way: White

info = color.get(1) # 2nd way:  White
print(info)

#without using get() # 3rd way: White
print(color[4])







# 10. setdefault():

person = {'Name': "Omkar", "Age": 22}
Work = person.setdefault('Location', "London")
info = person.setdefault('Computer')
print(Work)  # OP: London
print(info)  # OP: None
print(person)  # OP: {'Name': 'Omkar', 'Age': 22, 'Location': 'London', 'Computer': None}