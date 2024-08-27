
def calculator():
    # Taking input from user in float format
    num1 = float(input("Enter the First Value: "))
    num2 = float(input("Enter the Second Value: "))
    
    # Display operation options
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get the operation choice from the user
    operation = input("\nEnter your choice (1/2/3/4): ")
    
    # Arithmetic operation of calculator
    #Addition
    if operation == '1':
        result = num1 + num2
        print(f"\nThe result of {num1} + {num2} is: {result}")
    #Subtraction
    elif operation == '2':
        result = num1 - num2
        print(f"\nThe result of {num1} - {num2} is: {result}")
    #Multiplication
    elif operation == '3':
        result = num1 * num2
        print(f"\nThe result of {num1} * {num2} is: {result}")
    #Division 
    elif operation == '4':
        #checking that input of num2 is 0 or not
        if num2 != 0:
            result = num1 / num2
            print(f"\nThe result of {num1} / {num2} is: {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation choice.")

# Call calculator to run this program
calculator()
