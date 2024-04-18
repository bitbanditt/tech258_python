# Get requests from apis. Get data using api via url to create code

import requests

postcodes_req = requests.get("http://api.postcodes.io/postcodes/se120nb")
print(postcodes_req)
print(type(postcodes_req.status_code))
print(postcodes_req.headers)
print(type(postcodes_req.content))

print(postcodes_req.json())

data_dict = postcodes_req.json()["result"]
print(data_dict["region"])

# call from api quick and easy way to get data into python to use and work with it
# and build using it 

