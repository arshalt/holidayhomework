principal = float(input("Please enter Principal amount"))
if principal >= 10000:
    print(float(principal) * (6 / 100))
elif principal < 10000:
    print(float(principal) * (5 / 100))
