import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}

print(type(car_data))

# json.dumps() --> serialises (turns into string) json to a formatted string

car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# json.dump() --> Creates a stream object and expects a file object to write to

with open("new_json_file.json", "w") as jsonfile:  #2 arguements/parameters, the file to create, w to write in it
    json.dump(car_data, jsonfile) #as jsonfile so it can be referenced, car_data is the dictionary to become json

