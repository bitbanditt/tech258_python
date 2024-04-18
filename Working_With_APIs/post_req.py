# with post you need to send data via api

import requests
import json

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 60N", "EX165BL"]})
headers = {"Content-Type": "application/json"} # stating what type data being sent is in

post_multi_req = requests.post("http://api.postcodes.io/postcodes", headers=headers, data=json_body)
print(post_multi_req.json())

# data = -> accepts a string (so we had to use json.dumps first)
# json = -> accepts a python dictionary (many ways to do the same thing)