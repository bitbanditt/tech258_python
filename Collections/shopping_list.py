# Create a shopping list.

shopping_list = ["eggs","bread","bananas","biscuits","milk"]

# Print shopping list to the screen
# can cast as a string print("This is your shopping list: \n" + str(shopping_list))
# \n is like pressing enter. Starts on a new line

print(shopping_list)

# Print the data type of shopping_list

print(type(shopping_list))

# Print the first item in the list

print(shopping_list[0])

# Print the last item in the list

print(shopping_list[-1])

# Change the second item in the list to rice and print to verify change

shopping_list[1] = "rice"

print(shopping_list[1])

# Add the item carrots to the list using a method, not = to re assign

shopping_list.append("carrots")

print(len(shopping_list))

# Add another list with two items

forgotten_items = ["toffee", "coffee"]
shopping_list.extend(forgotten_items)

# Print shopping list to check items have been added

print(shopping_list)

# Remove bananas and print to check

shopping_list.remove("bananas")
print(shopping_list)

# Remove the last item and print to check
shopping_list.pop()
print(shopping_list)

# Use the append method to add an item to the list

shopping_list.append("Watermelon")


