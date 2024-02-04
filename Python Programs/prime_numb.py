num = int(input("Enter the number: "))

if num == 1:
    print("Not Prime Number")
elif num > 1:
    for i in range(2, num):
        if num%i==0:
            print("Not Prime number")
            break
    else:
        print("Prime Number")