import io
from .tideday import TideDay
from src.utilities import Utilities
import re

TIDE_COUNT = 4  # max of 4 tides in 1 day
DEBUG = False

def myprint(msg):
    if not DEBUG:
        return
    print(msg)

class TideMonth:

    month = None
    year = None
    tide_type = None
    formatted_tideday = None

    def __init__(self, tide_for_month, month: int, year: int = 2023 ):
        self.month = month
        self.year = year
        self.formatted_tideday = []
        for i in tide_for_month:
            if self.is_comment_line(i):
                continue

            temp_tide_type = self.get_tide_type(i)
            if temp_tide_type:
                self.tide_type = temp_tide_type
                continue

            td = TideDay(i, self.month, self.year, self.tide_type)
            self.formatted_tideday.append(td.GetFormattedDay())
            
    def get_formatted_tide_month(self):
        return self.formatted_tideday

    def save_tide(tide_1: int, tide_2: int, tide_3: int, tide_4: int, tide_date: int, is_high_tide: bool, tide_file: str):
        """
        Format tide data for a single day.
        'is_high_tide' is True if the first tide of the day (tide_1) is High, else False.
        Subsequent tides toggle between Low and High.
        There is not always a Tide 4 during a calendar day. Right now, this absence is
        indicated by a "9" in the input, and gets translated to "NA".
        Tide_n consists of [time, tide height] (to save keystrokes). For example,
        '0421327', means time - 04:21, height - 3.3 metres. (Note that new charts use 9.9 metres, not 9.99 metres)
        Full example:
        Date,tidalrange,type1,time1,height1,type2,time2,height2,type3,time3,height3,type4,time4,height4
        30/01/2022,2.77,04:33:00,High,3.44,10:53:00,Low,0.76,17:10:00,High,3.42,23:24:00,Low,0.67
        """
        if not Utilities().is_valid_date(tide_date):
            raise ValueError("date is not valid")
        tides = [tide_1, tide_2, tide_3, tide_4]
        tides_formatted = []

        tide_file = f"data/{tide_file}"

        formatted_tide_date = Utilities().get_tide_date(tide_date)
        myprint(f"formatted_tide date: {formatted_tide_date} ")
        for iteration, i in enumerate(tides):
            myprint(f"iteration {iteration}")
            tides_formatted.append("{:07}".format(i))
        
        myprint(tides_formatted)
        formatted_tide = ""
        for iteration, i in enumerate(tides_formatted):
            myprint(f"iteration b {iteration}")
            formatted_tide += ',' + Utilities().get_tide_instance(iteration, is_high_tide, i)
            myprint(formatted_tide)

        formatted_tide = formatted_tide_date + "," + str(Utilities().get_tidal_range(formatted_tide))  +  formatted_tide + "\n"
        myprint(f"formatted tides for day: {formatted_tide}")      
        with io.open(tide_file, "a") as f:
            f.writelines(formatted_tide)

        return tide_file

    def get_the_lines(self):
        lines = [
            'The Title',
            '',
            'First Header',
            'Header Two',
            '',
            'Some body and then some repeat all that until more than max for header',
            '2 First Header',
            '2 Header Two',
            '',
            '2 Some body and then some repeat all that until more than max for header',
            
        ]

        return lines

# If a line (ultimately from a csv) begins with #, it is a comment.
# Else it is data
# https://docs.python.org/3/howto/regex.html#regex-howto
    def is_comment_line(self, line):
        pattern = re.compile("#")
        match = pattern.match(line)
        if not match:
            return False
        return match.string == line

# A valid tide_type starts with (CI) 'low' or 'high'.
# If neither is true, return None
# Else return 'low' or 'high' (CS)
# We don't care if subsequent letters don't match. so e.g. "lowx" is a valid tide.
    def get_tide_type(self, candidate_tide_type):
        pattern_low = re.compile('low', re.IGNORECASE)
        pattern_high = re.compile('high', re.IGNORECASE)
        match = pattern_low.match(candidate_tide_type)
        if not match:
            match = pattern_high.match(candidate_tide_type)
            if not match: # neither high nor low matched
                return None
            else:
                return 'high'
        else: # low matched
            return 'low'

    # if an int, return True. Else false
    def parse_int(self, candidate_int):
        try:
            dummy_int = int(candidate_int)
        except ValueError:
            return False
        return True

# A tide_day record starts with 1 to 31, and is followed by a comma.
# If that is not true, return none. Else parse the elements, and
# return an object
# (more validation required than that)
    def get_tide_day(self, candidate_tide_day):
        elements = candidate_tide_day.split(",")
        tide_date = 0
        if self.parse_int(elements[0]):
            tide_date = (int) (elements[0])
        if tide_date > 0 and tide_date < 32:
            return tide_date
        return None



        
        
        
