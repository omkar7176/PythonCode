# length of the the string

fruit = "Apple"
len1 = len(fruit)
print(f"The fruit name is {fruit} and the length of that is {len1}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++

word = "ComputerProgramming"
a = slice(8)
print(word[a])
# OUTPUT = Computer

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++

player = "MahendraSingh"
slit1 = player[8:]
slit2 = player[:8]


print(player[::-1]) # --> String in reverse order -- > hgniSardnehaM
print(player[:])  # --> The same copy of player
print(player[2:5]) # --> hendraSing
print(player[-3:])  # --> ngh
print(slit1)   # --> Singh
print(slit2)   # --> Mahendra

