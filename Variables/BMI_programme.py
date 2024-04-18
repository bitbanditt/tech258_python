# Create a programme to check BMI

# Get the users height
print("What is your height in cm? ")

# Make the height a variable the user can input. Cast input to a float
height = float(input())

# Repeat the process for getting the users weight
print("What is your weight in kg? ")

weight = float(input())

# BMI is calculated by dividing the height by the square of the weight
# Square is also known as exponent which can be done with (value)**(square value)
BMI = height/weight**2

# Print the result as a string, as BMI is a float in cannot be concatenated (merged)
# with the string "your BMI is" Only similar data types can be concatenated
print("Your BMI is " + str(BMI))

# A way to better the code would be to print the result as a f-string to two decimal points

