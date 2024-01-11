for x in range(1, 11):    #(1, 11) --> printing from 1 to 10
    print(x)

# ++++++++++++++++++++++++++++++++++++++

for even in range(2, 22, 2):  #(2, 22, 2) --> 2=start loop from 2, 22=end point of loop, 2=Gap between the two numbers
    print(even)

# Output: Table of 2 / even numbers
    
# +++++++++++++++++++++++++++++++++++++++++++

for odd in range(1, 11, 2):
    print(odd)

# Output: odd numbers    
    
# +++++++++++++++++++++++++++++++++++++++++++    

# Iterating a String

name = "Omkar"
for i in name:
    print(i, end=" ")
    # print()

# +++++++++++++++++++++++++++++++++++++++++++ 

# Iterating over a list

color = ["Green", "White", "Blue", "Orange"]

for i in color:
    print(i, end=" ")
    print()


# +++++++++++++++++++++++++++++++++++++++++++ 

# Iterating over a Dictionary

comp = {'G': "Google", "A":"Amazon", "C":"Civo", "O":"oracle"}
for i in comp.keys():
    print(i, comp[i])

# +++++++++++++++++++++++++++++++++++++++++++

# Using else statement inside a for loop in Python

software = ['Adobe', 'PyCharm', 'Intellij_IDEA', 'VS_Code']
for i in software:
    print(i)
else:
    print("Cool")


# +++++++++++++++++++++++++++++++++++++++++++
# Using if-else in for loop with break statement

for i in range(1, 21):
    if(i == 15):
    # if(i == 35):    
        break
    else:
        print(i)

# +++++++++++++++++++++++++++++++++++++++++++
# Using if-else in for loop with continue statement

for i in range(1,11):
    if(i == 7):
        continue
    else:
        print(i)