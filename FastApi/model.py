import json

PEOPLE = "test/people.json"

def load_people():
    jsonFile = open(PEOPLE, "r")
    data = json.load(jsonFile) 
    jsonFile.close() 
    return data

def save_people(data):
    jsonFile = open(PEOPLE, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()                