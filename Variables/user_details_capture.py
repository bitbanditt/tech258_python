# Create a programme to collect a users details

# Greet the user and get their name
print("Hi, what is your name?: ")

# Make sure they input a string by casting the input as a string
name = str(input())

# Use the name variable to greet user and collect their age as an integer
print("Hi " + name + ", what is your age?: ")
age = int(input())

# Using the users name collect their address
print(name + ", what is your address?: ")
address = str(input())

# Return the users information to them using the correct casting and spacing.
# Remember you can only concatenate(merge) the same data type. Because part
# of the details are a string you need to type cast non strings to strings using (str)

print("Hi " + name + ", you are " + str(age) + " years old, and live at " + address)

# Ways to better the code would be to a) put the print message in the input function like so:
# input("what is your age?: "). to b) use code blocks like if else or a while loop to handle
# incorrect entries by printing a message asking for the desired type of input
