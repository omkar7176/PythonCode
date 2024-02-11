# Using the third variable --> temp
# Solution 1:
a = 10
b = 20

temp = a
a = b
b = temp

print("After swapping value of a: ", a)
print("\nAfter swapping value of b: ",b)




#Solution: 2

x = 30
y = 40

x,y = y,x

print("\nAfter swapping value of x: ", x)
print("\nAfter swapping value of y: ",y)