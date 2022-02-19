import io
from src.utilities import Utilities
import datetime
import re

TIDE_COUNT = 4  # max of 4 tides in 1 day
DEBUG = False

def myprint(msg):
    if not DEBUG:
        return
    print(msg)

def save_tide(tide_1: int, tide_2: int, tide_3: int, tide_4: int, tide_date: int, is_high_tide: bool, tide_file: str):
    """
    Format tide data for a single day.
    'is_high_tide' is True if the first tide of the day (tide_1) is High, else False.
    Subsequent tides toggle between Low and High.
    There is not always a Tide 4 during a calendar day. Right now, this absence is
    indicated by a "9" in the input, and gets translated to "NA".
    Tide_n consists of [time, tide height] (to save keystrokes). For example,
    '0421327', means time - 04:21, height - 3.27 metres.
    Full example:
    30/01/2022,04:33:00,High,3.44,10:53:00,Low,0.76,17:10:00,High,3.42,23:24:00,Low,0.67,2.77
    """
    if not Utilities().is_valid_date(tide_date):
        raise ValueError("date is not valid")
    tides = [tide_1, tide_2, tide_3, tide_4]
    tides_formatted = []

    formatted_tide = Utilities().get_tide_date(tide_date)
    myprint(f"formatted_tide date: {formatted_tide} ")
    for iteration, i in enumerate(tides):
        myprint(f"iteration {iteration}")
        tides_formatted.append("{:07}".format(i))
    
    myprint(tides_formatted)
    for iteration, i in enumerate(tides_formatted):
        myprint(f"iteration b {iteration}")
        formatted_tide += ',' + Utilities().get_tide_instance(iteration, is_high_tide, i)
        myprint(formatted_tide)

    formatted_tide += ',' +  str(Utilities().get_tidal_range(formatted_tide)) + "\n"
    myprint(f"formatted tides for day: {formatted_tide}")      
    tide_file = "data/tidetimes.csv"
    with io.open(tide_file, "a") as f:
        f.writelines(formatted_tide)

    return tide_file
