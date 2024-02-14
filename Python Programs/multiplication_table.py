# Multiplication Table

# Solution 1: Using for loop

a = int(input("Enter the number: "))

# for i in range(1,11):
#     print(a, "*", i, "=", a*i)

# OP:   2 * 1 = 2
#       2 * 2 = 4
#       .......
#       .......
#       2 * 10 = 20




# Solution 2: Using while loop
num = int(input("Enter the number: "))
i = 1

while(i <= 10):
    print(a, "*", i, "=", a*i)
    i+=1
else:
    print("Done")