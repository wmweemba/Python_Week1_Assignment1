"""This is a simpler calculator that requests user input of two numbers and an operation and then prints the result.
"""

# Request user input and convert it into an appropriate data type (float)
# A function is used to calculate the rsult of the operation
def calculator():
    num1 = float(input("Enter the first number: ")) # Converts the collected numbers into float data type
    num2 = float(input("Enter the second number: "))
    action = input("Enter the operation (+, -, *, /): ")

    # performs the check on what operator was given and calculates the result based on the input
    if action == '+':
        result = num1 + num2
    elif action == '-':
        result = num1 - num2
    elif action == '*':
        result = num1 * num2
    elif action == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"
    
    # prints out the final result
    return result

print(calculator())
    
