print("Please input the amount of sales")
a = float(input())
b = float(50000)
c = float(75000)
d = float(0.1)
e = float(0.15)
commission1: float = a * float(d)
commission2: float = a * float(e)
if a < b and a < c:
    print("Sorry, You do not meet the sales commission criteria")
if a >= b and not (a >= c):
    print(commission1)
    print(" ^ ")
    print("/ \ ")
    print(" |")
    print(" |")
    print(" |")
    print("This is with 10% commission")
if a >= c:
    print(commission2)
    print(" ^ ")
    print("/ \ ")
    print(" | ")
    print(" | ")
    print(" | ")
    print("This is with 15% commission")


