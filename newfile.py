print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Factorial")

Option = int(input("Choose an operation (1-5): "))

if Option in [1, 2, 3, 4]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if Option == 1:
        result = num1 + num2
    elif Option == 2: 
        result = num1 - num2
    elif Option == 3:
        result = num1 * num2
    elif Option == 4:
        if num2 != 0:
            result = num1 // num2  
        else:
            result = "Undefined (division by zero)"
    print("The result of the operation is: {}".format(result))

elif Option == 5:
    n = int(input("Enter a number: "))
    factorial = 1
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        for i in range(1, n+1):
            factorial *= i
        print(f"The factorial of {n} is {factorial}")

else:
    print(f"{Option} is an invalid option.")