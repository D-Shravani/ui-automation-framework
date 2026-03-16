import json

def load_data():

    with open("config/test_data.json") as file:
        return json.load(file)
