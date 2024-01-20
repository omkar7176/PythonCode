                    # ** Dictionary in Python 
# A dictionary in Python is a data structure that stores the value in value:key pairs.
# Note: The dictionary do not allow duplicates.but it contain same key which represent the updated value.


Details = {'Name': "Omkar", 'City': "Pune", 'Comp': "Microsoft"}
info = {1 : "Ram", 2 : "Delhi", 3 : "Amazon"}
print(Details)
print(info)




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