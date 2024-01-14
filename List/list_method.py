''' List_Methods: 
    1.  append()
    2.  insert()
    3.  extend()
    4.  sort()
    5.  pop()
    6.  remove()
    7.  copy()
    8.  count()
    9.  reverse()
    10. index() '''

'''1. append() --> we can only insert single element at a time.'''

color = ["red", "green", "white", "purple"]
color.append("orange")
print(color)
# OP: ['red', 'green', 'white', 'purple', 'orange']
# it store the new variable at the end





''' 2. insert() --> method have two parameters which is index no. & value, to add in the list. 
                    you can only one element add in the list'''

color = ["White", "black", "blue", "green", "orange"]
color.insert(1, "Red")
print(color)

# OP: ['White', 'Red', 'black', 'blue', 'green', 'orange']




''' 3. extend() --> concatenation of two list, there is no limit '''

colorA = ["A_red","A_blue","A_green","A_yellow"]
colorB = ["B_red","B_blue","B_green","B_yellow"]
colorB.extend(colorA)
print(colorB)

#OP: ['B_red', 'B_blue', 'B_green', 'B_yellow', 'A_red', 'A_blue', 'A_green', 'A_yellow']






''' 4.sort() --> sort the numbers in ascending order & alphabet letters are also sort in ascending
                 the capital letter will in first. '''

a = [7,6,4,9,5,0,1,2,8,3]
a.sort()
print(a)
# OP: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = ["Omkar", "Ram", "abhi", "Rutik", "Kunal", "saket"]
b.sort()
print(b)

#OP: ['Kunal', 'Omkar', 'Ram', 'Rutik', 'abhi', 'saket']
# first priority to capital letter & then sort

# ** If you want to print in descending order we must give -- sort(reverse=True) -- as a parameter in the sort method.

num = [7,6,4,9,5,0,1,2,8,3]
num.sort(reverse=True)
print(num) 
# OP: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]




''' 5. pop() --> removes the item from list.
                 pop() is delete the element using index number 
                 Syntax: list.pop(index_no)'''

# 1st Way

color = ["red", "green", "white", "purple"]
color.pop(1)
print(color)
# OP: ['red', 'white', 'purple']


# 2nd Way

color = ["red", "green", "white", "purple"]
x = color.pop(0)
print(x)
# OP: red





''' 6. remove() --> pop() is delete the element to add the element name in parameter
                    Syntax: list.remove(elmnt) '''

animal = ["cat", "dog", "horse", "cow", "sheep", "goat"]
animal.remove("sheep")
# print(animal)




''' 7. The copy() method returns a shallow copy of the list. '''

numbers = [2,4,6,8,10,12,14,16,18,20]
x = numbers.copy()
print(x)
# print(numbers)





''' 8. count(): Return the number of times the value 9 appears in the num list'''

num = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = num.count(9)
# print(x)
# OP: 2





''' 9. reverse(): reverse the order of the list.
                  Syntax: list.reverse()'''

test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test.reverse()
# print(test)





''' 10. index(): seraches a given element from the start of the list & returns the position of element'''

comp = ['Google', 'Amazon', 'Microsoft', 'Oracle', 'facebook']
print(comp.index('facebook'))
# OP: 4