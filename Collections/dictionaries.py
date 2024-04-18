# Dictionaries

# key = value pairs
# key is the reference, value is the data storage mechanism you want (int, string etc.)

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up"]

}

# Access value via key

print(student1["stream"])

# Access element in list value

print(student1["completed_lesson_names"][0])

# Amend key value

student1["completed_lessons"] = 3
print(student1["completed_lessons"])

# Removing a value from a key

#student1["completed_lesson_names"].remove("collections")
#print(student1)["completed_lesson_names"]

# Getting the keys for a dictionary

print(type(student1.keys()))