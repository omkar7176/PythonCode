# Example 1: While for name
name = input("Enter the name: ")

while name == "":
    print("You did not enter the name: ")
    name = input("Enter the name: ")

print(f"Hello {name}")

# Example 2: While for age

age = int(input("Enter the age: "))

while age < 0:
    print("The age is not negative.")
    age = int(input("Enter the age: "))

print(f"It is your {age} years old.")

# Example 3:

food = input("Enter the like (q to quiet): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter the another food like u (q to quiet): ")

print("bye")
