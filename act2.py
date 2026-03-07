num1 = float(input("ENTER YOUR FIRST NUMBER: "))
num2 = float(input("ENTER YOUR SECOND NUMBER: "))
num3 = float(input("ENTER YOUR THIRD NUMBER: "))

if num1 > num2 and num1 > num3:
    print("the largest number is", num1)
elif num2 > num3:
    print("the largest number is", num2)
else:
    print("the largest number is ", num3)