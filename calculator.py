def calculate(a,operator,b) :
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        if b==0 :
            return "Error : Cannot divide by zero"
        return a/b
    else:
        return "Invalid Error."


num1 = float(input("Enter first number: "))
operator = input("Enter operator +,-,*,/: ")
num2 = float(input("Enter second number: "))

print("Result: ", calculate(num1,operator,num2))