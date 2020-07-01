number_1 = float(input("Please input the first number"))
number_2 = float(input("Please input the second number"))
number_3 = float(input("Please input the third number"))
print("Type1 = number 1 + number 2")
print("Type2 = number 2 + number 3")
print("Type3 = number 1 + number 3")
print("Which sum do you want ?")

sum_type: str = str(input())

if sum_type:
    print(number_1 + number_2)
    print("This is Type 1")
if sum_type:
    print(number_2 + number_3)
    print("This is Type 2 ")
if sum_type:
    print(number_1 + number_3)
    print("This is Type 3 ")