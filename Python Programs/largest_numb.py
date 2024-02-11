num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1>num2 and num1>num3:
    print(f"Num1, {num1} is Largest Number")
elif num2>num1 and num2>num3:
    print(f"Num2, {num2} is Largest Number")
else:
    print(f"Num3, {num3} is Largest Number")       