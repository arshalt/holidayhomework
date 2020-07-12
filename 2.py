def largest_num(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3


number1 = float(input("Please enter the first number"))
number2 = float(input("Please enter the second number"))
number3 = float(input("Please enter the third number"))

print(largest_num(number1, number2, number3))
print("This is the biggest number")
