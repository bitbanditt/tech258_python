# Functions

# DRY - Don't Repeat Yourself
# if your going to use something again, put it in a function and call that cod
# makes code more efficient and have less lines

# function with no arguements

# def creates the function. you can give an arguemnt
#basic function
def print_something():
    print("something as been printed")

# function must be called
print_something()

def print_something(name):
    print("Hello, my name is" + name)

print_something(" Nick")

# function with arguement

def addition(int1, int2):
    return int1 + int2

print(addition(2,2))
print(addition(10, 15))

# default arguements

def addition(int1=2, int2=2):
    return int1 + int2

print(addition())
print(addition(int2=15))

# multiple arguements

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)

multi_args(1, 2, 4, 6, 7)
multi_args(1, 2)

# type hints

def division(denom: int, num: int) -> float:
    return denom / num

print(division(5, 3))