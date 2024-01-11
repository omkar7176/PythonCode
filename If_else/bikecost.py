try: 
    costprice = int(input("Enter the cost price of your bike: "))

    if(costprice>100000):
        print("The road tax you need to pay 15%.")
    elif(costprice>50000 and costprice<=1000000):
        print("The road tax you need to pay 10%.")
    elif(costprice<=50000):
        print("The road tax you need to pay 5%.")
    else:
        print("Pay the GST charges")


except Exception as e:
    print("Please enter the valid input ",e)