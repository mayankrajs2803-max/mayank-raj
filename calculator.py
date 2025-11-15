num1 = float(input("enter the number"))
num2 = float(input("enter the number"))
operator = input("enter the operator")
if operator == "+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("invalid operator")
