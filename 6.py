hra = int(input("Please enter HRA"))
da = int(input("Please enter DA"))
it = int(input("Please enter IT"))
if (int(hra) > 35) and (int(da) > 37) and (int(it) > 5):
    print("Your Salary is 40000")
elif (int(hra) > 25) and (int(da) > 32) and (int(it) > 6):
    print("Your Salary is 20000")
elif (int(hra) > 25) and (int(da) > 30) and (int(it) > 7):
    print("Your Salary is 10000")
