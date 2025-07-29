#4 function + %
def add():
    num1 = input("Enter Number 1: ")
    num2 = input("Enter Number 2: ")
    a = int(num1) + int(num2)
    print(a)
def sub():
    num1 = input("Enter Number 1: ")
    num2 = input("Enter Number 2: ")
    a = int(num1) - int(num2)
    print(a)
def mult():
    num1 = input("Enter Number 1: ")
    num2 = input("Enter Number 2: ")
    a = int(num1) * int(num2)
    print(a)
def div():
    num1 = input("Enter Number 1: ")
    num2 = input("Enter Number 2: ")
    a = int(num1) / int(num2)
    print(a)
def per():
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    a = num1 / num2
    b = a * 100
    print(b)
x = True  
while x:
    y = input("What would you like to do?: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Percent \n")
    if y == "1":
        add()
    if y == "2":
        sub()
    if y == "3":
        mult()
    if y == "4":
        div()
    if y == "5":
        per()
