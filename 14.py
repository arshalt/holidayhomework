def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


num1 = int(input("Please enter a number"))
num2 = int(input("Please enter a number"))

print("The H.C.F. is", compute_hcf(num1, num2))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)





def lcm(a, b):
    return (a * b) / gcd(a, b)


a = int(input("Please enter your number for LCM"))
b = int(input("Please enter your number for LCM"))
print('LCM of', a, 'and', b, 'is', lcm(a, b))
