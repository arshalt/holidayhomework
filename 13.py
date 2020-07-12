num = int(input("Please enter your number"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "Is is a prime")
else:
    print(num, "is not a prime number")