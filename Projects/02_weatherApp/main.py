import requests
import json
import os

url = f"https://api.github.com/users/paras-017"
response = requests.get(url).text                #response is in string
dictFormat = json.loads(response)                #response is in dict now

with open('data.py','w') as f:
    f.write(response)