x = int(input("Enter the number: "))

# Using if-else
if x%2 == 0:
    print(f"The number {x} is even")
else:
    print(f"The number {x} is odd")

#optinal:
# elif x%2 != 0:
#     print(f"The number {x} is odd")


#Using while loop
while(x%2)==0:
    print("The given number is even.")
    break
else:
    print("The given number is Odd.")