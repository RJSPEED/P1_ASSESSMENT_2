import requests
import json
import os

def get_name():
    print("Please input a name")
    return input()

#Get name from user
name = get_name()

#Retrieve API data
url_str = "https://pokeapi.co/api/v2/pokemon/" + name 
api_name = requests.get(url_str)
name_data = json.loads(api_name.text)

#Output data to JSON file
DIRECTORY = os.path.dirname(__file__)
FILENAME = name + "_data.json"
FILEPATH = os.path.join(DIRECTORY, FILENAME)

with open(FILEPATH, 'w') as file_object:
    json.dump(name_data, file_object, indent=2)

