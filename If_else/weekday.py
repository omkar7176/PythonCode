try:
    Day = int(input("Enter the number from 1 to 7: "))

    if(Day == 1):
        print("Monday")
    elif(Day == 2):
        print("Tuesday")
    elif(Day == 3):
        print("Wednesday")
    elif(Day == 4):
        print("Thursday")
    elif(Day == 5):
        print("Friday")
    elif(Day == 6):
        print("Saturday")
    elif(Day == 7):
        print("Sunday")

except Exception as e:
    print("Enter the valid input: ", e)