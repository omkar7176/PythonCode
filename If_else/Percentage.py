try: 
    per = float(input("Enter the percentage: "))

    if(per>90 and per<99.99):
        print("A Grade")
    elif(per>80 and per<=90):
        print("B Grade")
    elif(per>=60 and per<=80):
        print("C Grade")
    elif(per<60 and per>=35):
        print("D Grade")
    else:
        print("Fail")
except Exception as e:
    print("Please enter the valid input", e)            