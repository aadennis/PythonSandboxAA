import json
import pandas as pd

def read_voicings():
    # with open("pa/voicings.json","r") as f:
    #     voicings_map = json.load(f)
    # print(voicings_map)

    df = pd.read_json("pa/voicings.json")
    print(df)

read_voicings()    