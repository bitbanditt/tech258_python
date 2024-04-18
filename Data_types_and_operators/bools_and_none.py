# Booleans and None

# Booleans can be true or false

a = True
b = False

print(a == b) # False
print(a != b) # True


# What hsppens when you try and convert a string to a bool (using casting)?

#Always True unless the string is empty
print(bool("a")) # True
print(bool("")) # False

# The value of None

# None is an object, it is essentially a placeholder

# None != False

x = None

print(x == False) # False
print(x == None) # True

# None is best used over an empty string etc. It is less likley to cause issues down the line