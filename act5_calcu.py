print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter choice (1/2/3/4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == "1":
    answer = a + b
    print("Result:", answer)

elif operation == "2":
    answer = a - b
    print("Result:", answer)

elif operation == "3":
    answer = a * b
    print("Result:", answer)

elif operation == "4":
    if b != 0:
        answer = a / b
        print("Result:", answer)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid choice.")