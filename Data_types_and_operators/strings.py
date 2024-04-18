# Strings

single_quotes = 'Look! Single quotes'
double_quotes = "Look! Double quotes"

print(single_quotes)
print(double_quotes)

# Double quotes generally preffered as ' can have other uses

# bad_string = 'It's not right'
good_string = "It's not right"

# if you really want to use single quotes
escape_example = 'I said \'Wow!'

# String Indexing

Hw = "Hello World"

# Find out how many characters are in this string using an inbuilt python method
print(len(Hw))

# Target just the first character (H) using string indexing
print(Hw[0])

# Target the last character
print(Hw[10])
print(Hw[-1]) # better as it doesn't matter how long the string is

# Use negative indexing to get the second to last character (l)
print(Hw[-2])

# Bonus use string slicing to get the first three characters only
print(Hw[0:3]) # you can leave blank :3 and not 0 as it goes from start and stops at index 3

print(Hw[-3:]) # leaving end blank means it will start where asked and complete string

# String Methods

White_Space = "Lot's of whitespace at the end                              "
print(len(White_Space))
print(len(White_Space.strip()))


# F-strings

name = "Lassie"
years = 7
height_cm = 60.2

#print(f"{name} is {years} years old and {height_cm} tall)

name = "Snoopy"
years = 52

print(f"{name.upper()} is {years * 7} years in dog years")

# using f-strings to format numbers

pi = 3.14159265359

#Use an f-string to print



