x = '''
Operators:
1. Addition(+)
2. Subtraction(-)
3. Multiplication(*)
4. Division
'''
print(x)
y = ""

loop = "true"
while loop == "true":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Select an operator: ")

    if op == "1":
        print(num1+num2)
        print(y)
    elif op == "2":
        print(num1-num2)
        print(y)
    elif op == "3":
        print(num1*num2)
        print(y)
    elif op == "4":
        print(num1/num2)
        print(y)
    else:
        print("Invalid operator!")
