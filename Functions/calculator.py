# Create a calculator to do simple sums
# Break it down. Ask for inputs then create a function for each method of calculation

# First decide the operations you want the calculator to be able to perform.
# We'll do a simple add, subtract, multiply and divide. Define these functions

def add(x, y):
    return(x + y)

def subtract(x, y):
    return(x - y)

def multipy(x, y):
    return(x * y)

def divide(x, y):
    return(x / y)

# Ask user for the operation the want to use. (run code after to check, its good habit.)

print("Select operation: ")
print("+ to add")
print("- to subtract")
print("* to multiply")
print("/ to divide")

# Create a while true loop that runs the calculation options if a given condition is true
# As long as the loop evaluates to true the loop runs indefinitely, so we use a break to exit
#This allows the user to keep running calculations

while True:
    # Take an operation from the user
    operation = input("Choose an operator: + - * / :  ")

    # Check the user has picked a valid option using 'in' operator,
    # 'in' operator checks a value is inputted that matches a value in a list you provide
    # and returns it as a boolean value. True if in the sequence False if not

    if operation in("+", "-", "*", "/"):
        #try is a error handling method
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter a second number: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
        if operation == "+":
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == "-":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operation == "*":
            print(num1, "*", num2, "=", multipy(num1, num2))

        elif operation == "/":
            print(num1, "/", num2, "=", divide(num1, num2))

        # Check if the user wants to do another calculation. Break loop if answer is no.

        next_calculation = input("Would you like to do another calculation? yes/no: ")
        if next_calculation == "no":
            break
        else:
            print("Great!")
































