try:
    Day = int(input("Enter the number from 1 to 7: "))

    if(Day == 1):
        print("Sunday")
    elif(Day == 2):
        print("Monday")
    elif(Day == 3):
        print("Tuesday")
    elif(Day == 4):
        print("Wednesday")
    elif(Day == 5):
        print("Thursday")
    elif(Day == 6):
        print("Friday")
    elif(Day == 7):
        print("Saturday")

except Exception as e:
    print("Enter the valid input: ", e)