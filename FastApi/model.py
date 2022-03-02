import json

data = []

def load_people():
        jsonFile = open("people.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        # tmp = data["location"] 
        # data["location"] = path
        # data["mode"] = "replay"
        return data
        # data.append({"id":6,"first_name":"DooDah","last_name":"McCarlich","email":"emccarlich4@mit.edu",
        #     "ip_address":"43.123.149.96","trade":"Plasterers"})

        # ## Save our changes to JSON file
        # jsonFile = open("people.json", "w+")
        # jsonFile.write(json.dumps(data))
        # jsonFile.close()