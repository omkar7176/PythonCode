# Factorial of numbers:
# 1) 5! = 5*4*3*2*1
# 2) 4! = 4*3*2*1
# 3) 3! = 3*2*1
# 2) 2! = 2*1

# Conditions:
# 1. Cannot use for -ve numbers --> num<0  ❌ 
# 2. num == 0 --> factorial of that 0 is --> 1.

# Solution 1: Using for loop

num = int(input("Enter the number: "))

fact = 1

if num < 0:
    print("")
if num == 0:
    print("", 1)
if num > 0:
    for i in range(1, num+1):
        fact = fact*i
print("The Factorial of given number is: ", fact)
