# Create a waiter helper script that act like a real waiter taking orders

# Greet user

print("Good evening sir")

# print a list of starters and take an input

starters = ["shrimp", "garlic bread", "salad", "chicken wings"]
print("Here are our starters " + starters)
input(print("Here are our What would you like? " + str(starters)))
starter_order = input()

# print a list of mains and take an input

mains = ["steak and chips", "salmon with fresh salad", "grilled chicken burger and potato wedges"]
input(print("Here are our mains. What would you like? " + str(mains)))
main_order = input()

# print a list of desserts and take an input

desserts = ["cheesecake", "icecream", "brownie"]
input(print("Here are our desserts. What would you like? " + str(desserts)))
dessert_order = input()

# print all of the user choices

full_order = starter_order + main_order + dessert_order

print("You have ordered" + str(full_order))