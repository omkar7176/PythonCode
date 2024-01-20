#                                          ** tuple Methods **

# 1. count()

color = ("red", "yellow", "black", 'red', "black", "red")
paint = color.count('red')
print('The count of red is: ', paint)
# OP: The count of red is:  3


# 1.1 Counting the tuple & list as element

numb = (0, (1,2), 3, (1,2), (1,2), 4, 5, (1,2))
key = numb.count((1,2))
print("The count of (1, 2): ",key)





# 2. index() 

# Syntax : tuple.index(element, start, end)
# start & end is optional

fruit = ("Apple", "Mango", "pineapple", "grapes", "chiku", "Papya")
a = fruit.index('chiku')
print("The index of chiku: ", a)

b = fruit.index('grapes', 3, 5)
print("The index of grapes: ", b)



# 2.1 Using index the file is not found

numb = ('1', '2', '3', '4', '5', '6', '7', '5','5', '6', '7')

# num1 = numb.index('10')
# print(num1)


# use the tuple() function for list like convertig the list into tuple.

aqua = tuple(["Om", "kunal", "Shyam", "ram"])
print(aqua)
print(type(aqua))


# convert the list into tuple

x  = tuple([1,2,3,4,5])
print(type(x))
# OP: <class 'tuple'>





# accessing the values using slicing technique
names  = (1, "Omkar", 2, 3, 4, 5, "Shyam", "Kunal")
# 1st 
print(names[2:6])
#2nd
candidate = names.index("Shyam")
print(candidate)
#3rd
print(names[6])






# deleting the tuple

tuple1  = ("Omkar", "ram", "kunal")
del tuple1
print(tuple1)






# Also we can use the some common funnction iwith tuple
#  1. len()
#  2. max()
#  3. min()
#  4. sum()
#  5. sorted()  #--> It returns a new sorted list containing the elements of the tuple. 