try: 
    import calendar as calender
    from datetime import date
    today = date.today()
    print("Today: ", today)
    month = int(input("Enter the number for month: "))

    if(month == 1):
        print(calender.month(2024, 1))
    elif(month == 2):
        print(calender.month(2024, 2))
    elif(month == 3):
        print(calender.month(2024, 3))
    elif(month == 4):
        print(calender.month(2024, 4))
    elif(month == 5):
        print(calender.month(2024, 5))
    elif(month == 6):
        print(calender.month(2024, 6))
    elif(month == 7):
        print(calender.month(2024, 7))
    elif(month == 8):
        print(calender.month(2024, 8))
    elif(month == 9):
        print(calender.month(2024, 9))
    elif(month == 10):
        print(calender.month(2024, 10))
    elif(month == 11):
        print(calender.month(2024, 11))
    elif(month == 12):
        print(calender.month(2024, 12))
    else:
        print("Enter the number: ")    

except Exception as e:
    print("Enter the Valid Input: ", e)