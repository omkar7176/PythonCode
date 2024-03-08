#                         ** Sets Methods **

# 1.add(): Adds a given element to a set.
# 2.clear(): Removes all elements from the set.
# 3.copy(): 
# 4.difference(): 
# 5.difference_update(): 
# 6.discard(): Removes the element from the set.
# 7.intersection():
# 8.intersection_update()
# 9.pop()
# 10.remove(): Removes the element from the set.
# 11.union(): Returns a set that has the union of all sets.
# 12.update(): Adds elements to the set
# 13.symmetric_difference_update()
# 14.symmetric_difference()



# 1. add(): 

# --> it will add at the elements at random place because set haven't indexing.
# --> add() takes exactly one argument. we can't add the two elements at single time.
# --> you can't concatenate the two different sets using the add() method.

device = {"mouse", "keyboard", "moitor"}
device.add("Headset")
print(device)
# OP: {'mouse', 'moitor', 'Headset', 'keyboard'}






# 2. update():
# How to add items from another set into the current set
# --> there is no need to create third variable to add the two set. like "c = hardware.update(software)"

hardware = {"Mouse", "keyboard"}
software = {"VS Code"}
hardware.update(software)
print(hardware)
# OP: {'VS Code', 'keyboard', 'Mouse'}





# 3. remove():
#removing the set elements 
# --> remove() takes exactly one argument
#--> No need to create the third variable to print the set.

A = {"white", "blue","green", "black"}
A.remove("black")
print(A)
# OP: {'blue', 'green', 'white'}





# 4.discard():
#removing the items using discard() methods in sets.
#--> No need to create the third variable to print the set.
color = {"white", "blue","green", "orange"}
color.discard("blue")
print(color)
# OP: {'green', 'white', 'orange'}





# 5. pop():
# Note: Don't use the pop() in set becoz it will raise error & you will get the wrong output. 
#The pop() removes the last element from the (set, list, tuple) but set haven't the indexing, set print the elements randomly so it will remove the element from set as randomly & you will get the wrong output, so don't use the pop() in set.

# Example:
ele1 = {"white", "blue","green", "black"}
ele2 = ele1.pop()
print(ele2)
# OP: black  --> every time it show another output.


col = {"white", "blue","green", "black"}
col.pop()
print(col)
# OP: {'blue', 'black', 'green'}





# 6: clear():
ab = {"om", "john", "shon", "monty"}
ab.clear()
print(ab)
OP: set()