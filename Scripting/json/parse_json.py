# Parsing is converting strings into structured data

import json

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car["name"])
    print(car["engine"])

#same thing as above just not using with to open

path_to_json = "example.json"
json = json.load(open(path_to_json))
value = json["name"]

print(value)

# loads exmpample
 path_to_json = "example.json"
 json = json.loads(open(path_to_json).read()) # .loads expects a string, .read turns this into one
 value = json["name"]

 print(value)

 # json .load takes a file
 # json .loads takes a string