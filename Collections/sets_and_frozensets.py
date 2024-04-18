# Sets and Frozen sets

# Create a set

fruits = {"apple", "peach", "cherry"}
print(fruits)

# Sets are UNORDERED and UNINDEXED (they are unordered and are not numbered)

# Add an element
fruits.add("pear")
print(fruits)

# Remove an element
fruits.remove("apple")
print(fruits)

# Attempt to add a duplicate
# There can be no duplicates in a set. Trying won't cause an error, nothing will happen
fruits.add("peach")
print(fruits)

# Convert list to a set to remove duplicates
example = ["one", "two", "three","one"]
no_dupes = set(example)
print(no_dupes)

# Intergers are a bit weird as maybe because of memory it will print them in order

int_set = {1, 2, 3, 4}
print(int_set)

# Set operations

set_a = {}
set_b = {}

# Frozen set --> IMMUTABLE SET

frozen_set = frozenset(["hello", "world"])
print(frozen_set)

# frozen_set.add("!")
# print(frozen_set)

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)