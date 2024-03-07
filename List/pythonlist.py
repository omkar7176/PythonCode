#  ** List in Python **

''' Duplicate values in list '''
color = ["red", "yellow", "blue", "white", "red"]  #--> red
print(color)
# OP: ['red', 'yellow', 'blue', 'white', 'red']





 ''' length of the list ''' 
name = ["Omkar", "Ram","Shyam", "John", "Rocky"]
print(len(name))
# OP : 5




 ''' Add the mutiple types of elements '''

string = ["Omkar", 21, True, 1.23, 'r']
#  str + int + boolean + float + character 
print(string)
# OP: ['Omkar', 21, True, 1.23, 'r']




''' type of the list can define '''

name = ["Omkar", 21, True, 12.50, 'r']
print(type(name))
# OP: <class 'list'>




''' list defined as the construtor --> Don't use '''
name = list(("John", "ronny", "alex", "rocky"))
print(name)
print(type(name))
# OP: ['John', 'ronny', 'alex', 'rocky']
#     <class 'list'>




 '''Access the items from the list '''
element = ["mouse", "keyboard", "monitor","headphone", "laptop", "table", "stand", "mike"]
print(element[2])
# OP: monitor


''' Range of index & access it, also called as string slicing '''

hardware = ["mouse", "keyboard", "monitor","headphone", "laptop", "table", "stand", "mike"]
print(hardware[2:6])
# OP: ['monitor', 'headphone', 'laptop', 'table']



''' leaving out of the staring & ending value '''

print(hardware[3:])
# OP: ['headphone', 'laptop', 'table', 'stand', 'mike']

print(hardware[:3])
# OP: ['mouse', 'keyboard', 'monitor']


''' negtive indexing '''

print(hardware[-5:-2])
# OP: ['headphone', 'laptop', 'table']

print(hardware[-4:])
# OP: ['laptop', 'table', 'stand', 'mike']

print(hardware[:-2])
# OP: ['mouse', 'keyboard', 'monitor', 'headphone', 'laptop', 'table']

print(hardware[::2])
# OP: ['mouse', 'monitor', 'laptop', 'stand']





 ''' Checking the items in the list  '''
string = ['A', 'B','C','D','E','F']
if 'B' in string:
    print("Yesss")
# OP: Yesss    




 ''' Changing items value in list '''

name = ["Omkar", "Ram", "Shyam","Suraj", "Rocky"]
name[1] = "Ronny"
name[2] = "Sanket"
print(name)
# OP: ['Omkar', 'Ronny', 'Sanket', 'Suraj', 'Rocky']




''' Changing the range of  items of values in items '''

food = ["Tea", "coffee", "biscuit", "pizza", "burger", "coke"]
food[1:3] = ["Sandwich", "fries"]
print(food)
#OP: ['Tea', 'Sandwich', 'fries', 'pizza', 'burger', 'coke']



''' adding the 2 values with replacemnt of value 1. '''

color = ["red", "yellow", "white", "blue","pink","black"]
print("length of list before replace: ", len(color))
color[1:2] = ["orange", "brown"]
print(color)
print("length of list after replace: ", len(color))
# OP: length of list before replace:  6
# ['red', 'orange', 'brown', 'white', 'blue', 'pink', 'black']
# length of list after replace:  7




''' changing of 1 value replacing the 2 values in list '''

animal = ["dog", "cat", "horse", "duck", "tiger", "lion"]
animal[1:3] = ["puppy"]
print(animal)
#OP: ['dog', 'puppy', 'duck', 'tiger', 'lion']