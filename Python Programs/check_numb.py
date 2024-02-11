num = input("Enter the number: ")
try:
    if (num > 0):
        print("Positive number")
    elif(num == 0):
        print("Zero")
    elif(num < 0):
        print("Negative number")
    else:
        print("Invalid input...")
except Exception as e:
    print(e)
