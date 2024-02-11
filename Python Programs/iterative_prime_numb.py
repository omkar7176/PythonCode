x = int(input("Enter the upper limit here: "))
y = int(input("Enter the lower limit here: "))

for num in range(x , y+1):
    if num > 1:
        for i in range(2, num):
            if num%i==0:
                # print("Not Prime Number")
                break
        else:
            print("Prime Number: ", num)