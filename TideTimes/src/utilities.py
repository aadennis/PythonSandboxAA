from os import replace
import re
import datetime
import logging

class Utilities():
    def __init__(self):
        pass

    LOW_TIDE_FIRST = ["low", "high","low", "high"]
    HIGH_TIDE_FIRST = ["high","low", "high","low"]

    DEBUG = False

    def myprint(self, msg):
        if not self.DEBUG:
            return
        print(msg)

    @staticmethod
    def expand_abbreviations(abbreviated_text):
        """
        3112
To reduce keystrokes, replacement rules are:
h/H => High
anything else => Low
/ => :
"""
        Utilities().myprint(abbreviated_text)
        return abbreviated_text.upper().replace('H', 'High').replace('L', 'Low').replace('/', ':')

    def get_tidal_range(self, raw_tidal_data):
        """
        Given a comma-separated string, being different elements of a tide-day, extract
        the floats, assuming these are the tide heights (in metres, FWIW).
        The Tidal Range is then defined as the difference between the highest tide during the
        day, and the lowest.
        """
        tide_list = []
        for i in raw_tidal_data.split(","):
            if self.is_float(i):
                tide_list.append(float(i))
        self.myprint(tide_list)
        min_tide = min(tide_list)
        max_tide = max(tide_list)
        return round(max_tide - min_tide,2)

    def get_tidal_range2(self, raw_tidal_data):
        """
        Given an array where each element has 7 digits, being the 4 tides in a tide-day, extract
        the tide heights (ignoring the time data). 
        For info, the tide height is the last 3 of the 7 digits in each field:
            1.time of day: 4 digits, e.g. 0134 = 01h34m
            2.tide height: 3 digits, e.g. 113 = 1.13 metres;
        The Tidal Range is then defined as the difference between the highest tide during the
        day, and the lowest.
        "NA" tides, effectively null tides, should be ignored, but are not yet.
        """
        tide_list = []
        for i in raw_tidal_data:
            tide = float(f"{i[4:5]}.{i[5:8]}")
            tide_list.append(tide)
        self.myprint(tide_list)
        min_tide = min(tide_list)
        max_tide = max(tide_list)
        return round(max_tide - min_tide,2)

    
    def get_tide_position(self, first_tide, index):
        """
        Given the current index in the tide day (0-3),
        return the correct tide relative to the first tide of the day.
        For example, if the first_tide is 'low', then for an index of 0, return 'low'.
        For an index of 1, return 'high', 2 => low, 3 => high.
        """
        if first_tide == 'low':
            return self.LOW_TIDE_FIRST[index]
        else: # high tide is first
            return self.HIGH_TIDE_FIRST[index]



    @staticmethod
    def is_float(candidate_float):
        """
        Check if the value is a float.
        :param candidate_float: string to be checked
        :return: If the passed value is a float, return true, else false
        """
        try:
            float(candidate_float)
        except ValueError:
            return False
        return True

    def is_alpha(self, char):
        """
        Handles single characters only.
        True if between a-z or A-Z
        Else False
        """
        len_char = len(char)
        if len_char != 1:
            raise ValueError("is_alpha: expected 1 char, got [{}]".format(len_char))
        pattern = re.compile(r'[a-zA-Z]')
        ok = pattern.search(char)
        if not ok:
            return False
        return True

    def is_valid_watermark(self, water_mark):
        """
        A watermark has:
        (DEPRECATED)1. H or L, being high or low water. For this check, h/H is taken
        as high, any other character is low.
        https://medium.com/analytics-vidhya/regex-in-python-a-z-88ebf1c8fed4
        2. A time in the format HHSS
        3. A height in the format MCC, e.g. 321 being 3 metres and 21 cm
        The total characters must be 8 (1 + 4 + 3)
        Valid example 1: "h2111312", meaning 'high water is at 21.11, 
        with height of 3.12 metres'
        Valid example 2: "x0001001", meaning 'low water is at 00.01, 
        with height of 0.01 metres'
        
        """
        pattern = re.compile(r'^([0-1][0-9]|[2][0-3])([0-5][0-9])([0-9]{3})$') # e.g. a2359132
        ok = pattern.search(water_mark)
        if not ok:
            return False
        return True

    def get_high_low_marker(self, index, hl_marker):
        """
        For a given index, determine if that tide is a high or a low.
        hl_marker is 1 of True/False
        False means "the first tide of the day was a low tide".
        Following that example, the 2nd will be a high, the 3rd a low again,
        and the 4th a high again, assuming there is a 4th tide day on a give
        day.
        That principle is reversed for High tides.
        """
        logging.info("ctr/ hl_marker: {}/{}".format(index, hl_marker))
        high_low = None
        if index%2 == 0:
            if hl_marker:
                high_low = "High"
            else:
                high_low = "Low"
        else: # it's the reverse
            if hl_marker:
                high_low = "Low"
            else:
                high_low = "High"
        return high_low


    def get_tide_instance(self, ctr: int, hl_marker: bool, tide: int):
        """
        A tide instance is the combination of:
        time, whether high or low, the height.
        Output example: 3.27,High,01:56:00.
        Special case / magic number: if tide is "9", then
        return "NA,NA,NA"
        """
        NO_TIDE = "0000009"
        if tide == NO_TIDE:
            return "NA,NA,NA"
        high_low = self.get_high_low_marker(ctr, hl_marker)
        self.myprint(f"point a {tide}/{high_low}")
        raw_time  = tide[0:4]
        formatted_time = str(datetime.datetime.strptime(raw_time, "%H%M"))[11:]
        height = str(float(tide[4:])/100)
        tide_instance = "{},{},{}".format(high_low, formatted_time, height)
        self.myprint(tide_instance)
        return tide_instance

    def get_tide_instance2(self, ctr: int, hl_marker: bool, tide: int):
        """
        A tide instance is the combination of:
        time, whether high or low, the height.
        Output example: High,3.27,01:56:00.
        Special case / magic number: if tide is "9", then
        return "NA,NA,NA"
        """
        NO_TIDE = "0000009"
        if tide == NO_TIDE:
            return "NA,NA,NA"
        tide = str(tide)
        high_low = self.get_high_low_marker(ctr, hl_marker)
        self.myprint(f"point a {tide}/{high_low}")
        raw_time  = tide[0:4]
        print(raw_time)
        formatted_time = str(datetime.datetime.strptime(raw_time, "%H%M"))[11:]
        height = str(float(tide[4:])/100)
        tide_instance = "{},{},{}".format(high_low, formatted_time, height)
        self.myprint(tide_instance)
        return tide_instance

    def get_tide_date(self, ddmm):
        CURRENT_YEAR = "2022"
        return "{}/{}/{}".format(ddmm[2:4],ddmm[0:2], CURRENT_YEAR)


    def is_valid_date(self, tide_date):
        """
            A valid date has the entry format MMDD - example 0731.
            Later, we assume the year to always be the current year,
            right now that is a constant.
        """
        CURRENT_YEAR = "2022"
        month = tide_date[0:2]
        day = tide_date[2:4]
        self.myprint(month)
        self.myprint(day)
        
        candidate_date = CURRENT_YEAR + str(month) + str(day)
        try:
            datetime.datetime.strptime(candidate_date, '%Y%m%d')
            return True
        except ValueError:
            return False
                