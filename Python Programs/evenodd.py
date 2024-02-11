x = int(input("Enter the number: "))

# Using if-else
if x%2 == 0:
    print(f"The number {x} is even")
elif x%2 != 0:
    print(f"The number {x} is odd")
else:
    print("Even & Odd number program")



#Using while loop
while(x%2)==0:
    print("The given number is even.")
    break
else:
    print("The given number is Odd.")