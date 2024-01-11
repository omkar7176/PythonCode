# Question 1:
for x in range(5):
    for y in range(5):
        print("*", end=" ")
    print()

# Output:
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *  


# Question 2:

n = 5
for col in range(1, n+1):
    for row in range(1, col+1):
        print("*", end=" ")
    print()    

# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *     