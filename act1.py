x = 300

def find_closest(a, b, c):
    global x


a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

closest = min([a, b, c], key=lambda n: abs(n - x))
print("closest number to", x, "is", closest)