# 1. Simple tuple 
a = ("Omkar", "Ram", "Shyam")
print(a)
print(type(a))





# 2. Multiple data type
b = ("Omkar", 22, 'True', 23.1, )
print(b)
print(type(b))





# 3. Nested tuple
c = ("Omkar", [20, 'Ram'], 25, "kunal", 'True')
print(c)
print(type(c))





# 4. Tuple indexes

# ** Positive indexing
city = ("Pune", "Banglore", "Delhi", "Mumbai")
print(city[0])
print(city[1])
print(city[2])
print(city[3])

# **Ngeative indexing

animal = ("dog", "cat", "duck", "cow", "tiger", "goat")
print(animal[-1])
print(animal[-2])
print(animal[-3])
print(animal[-4])
print(animal[-5])
print(animal[-6])






# 5. Check for item:
name = ("Omkar", "Ram", "Shyam", "kunal")
a = input("Enter the name: ")
if a in name:
    print("Yess")
else:
    print("No")