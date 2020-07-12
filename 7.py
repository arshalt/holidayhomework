percentage = int(input("Please enter your percentage of marks"))
if 90 <= percentage:
    print("Your grade is A++")
elif 90 > percentage > 80:
    print("Your grade is A+")
elif 80 > percentage > 75:
    print("Your grade is A")
elif 75 > percentage > 60:
    print("Your grade is B")
elif 60 > percentage > 50:
    print("Your grade is C")
elif 50 > percentage > 40:
    print("Your grade is D")
elif 40 > percentage:
    print("You have FAILED")