#                         ** Sets Methods **

# 1.add(): Adds a given element to a set.
# 2.update(): Adds elements to the set
# 3.remove(): Removes the element from the set.
# 4.discard(): Removes the element from the set.
# 5.pop(): remove the last element from the Set.
# 6.clear(): Removes all elements from the set.
# 7.union(): Returns a set that has the union of all sets.
# 8.intersection_update()
# 9.intersection():
# 10.symmetric_difference_update()
# 11.symmetric_difference()



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





# 6. clear():
ab = {"om", "john", "shon", "monty"}
ab.clear()
print(ab)
# OP: set()






# 7. del 
# Del keyword is used to delete the set completely
abc = {12,14, 21.5, "Omk", "ram"}
del abc






# 8. union():
# How to join the two sets by using union() and update()
# 1. union()--> it needs to create the 3rd variable to combine the two sets. otherwise it will show you the wrong output.

colA = {'o', 'k'}
colB = {'B', 'y', 'e'}
colC = colA.union(colB)
print(colC)
# OP: {'e', 'y', 'o', 'B', 'k'}


# 2. update(): No need to create the 3rd varible to commbine two sets becoz after creating the 3rd variable, it shows the "none" OP.

colA.update(colB)
print(colA)
# OP: {'B', 'e', 'o', 'y', 'k'}





# 9: intersection_update(): Keep only duplicate items
# No need to create the 3rd varible otherwise it shows "None" OP.
x = {"Apple", "Cherry", "Grapes"}
y = {"PineApple", "Apple", "Banana"}
x.intersection_update(y)
print(x)
# OP: {'Apple'}
# Note: It shows the only duplicate elemnts in sets.






# 10. intersection(): 
# using intersection() method it needs to create the 3rd variable.
z = x.intersection(y)
print(z)
# OP: {'Apple'}
# Note: It shows the only duplicate elemnts in sets.





# 11. symmetric_difference_update():
# Keep all, but NOT the duplicates of common items

colorA = {"Red", "Black", "White"}
colorB = {"Orange", "Green", "White"}
colorA.symmetric_difference_update(colorB)
print(colorA)
# OP: {'Red', 'Black', 'Green', 'Orange'}






# 12. symmetric_difference():

z=colorA.symmetric_difference(colorB)
print(z)
#OP: {'Green', 'Black', 'Orange', 'Red'}