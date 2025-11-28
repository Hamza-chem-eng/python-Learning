def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return 0
    else:
        return a/b
a = float(input("enter first number :"))
o = input("enter the op (/,*,-,+) : ")
b = float(input("enter the second number :"))
if o == "/":
    if b == 0:
        print("Error")
    else:
        print(divide(a,b))
elif o == "*":
    print(multiply(a,b))
elif o == "-":
    print(subtract(a,b))
elif o == "+":
    print(add(a,b))
else:
    print("Error")
