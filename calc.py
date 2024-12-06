def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Input Number1: "))
            num2 = float(input("Input Number 2:"))
        if choice == '1'
            print(num1, "added to", num2, "equals", add(num1, num2))
        else if choice == '2':
            print(num1, "With", num2, "taken from it equals", subtract(num1, num2))
        else if choice == '3':
            print(num1, "multiplied by", num2, "equals", multiply(num1, num2))
        else if  choice == '4':
            print(num1, "divided by", num2, "leaves you with", divide(num1, num2))
