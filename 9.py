number = int(input("Enter a number"))
total = 0
while number > 0:
    digit = number % 10
    total = total+ digit
    number = number // 10
print("The total sum of digits is", total)
