cost_price = int(input("Please enter Cost Price"))
selling_price = int(input("Please enter Selling Price"))

if selling_price > cost_price:
    print ("This is the profit")
    print(selling_price - cost_price)
    print("Thank you for using this program")
elif cost_price > selling_price:
    print("This is the loss")
    print(cost_price - selling_price)
    print("Thank you for using this program")
