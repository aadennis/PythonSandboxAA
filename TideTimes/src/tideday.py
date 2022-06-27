"""
A manager for tide details for a given day in a month.
tide_day_record (passed to ctr) breaks down thus:
Field 1 - date in month
Field 2,3,4,5 - each of these is 7 digits in two sections:
1.time of day: 4 digits, e.g. 0134 = 01h34m
2.tide height: 3 digits, e.g. 113 = 1.13 metres;

Note that comments from the source file never reach this class, as they
are removed by class TideMonth
"""
from src.utilities import Utilities


class TideDay:

    items = None
    tide_date = None
    tide_month = None
    tide_type = None
    tide_times = []
   
    def __init__(self, tide_day_record, month, year, tide_type):
        self.tide_times = []
        self.validate_record(tide_day_record, month, year, tide_type)
        
    # validate the data passed to the constructor.
    # If validation passes, store the data in the object.
    # Else throw exceptions at the first validation error met.
    def validate_record(self, tide_day_record, month, year, tide_type):
        self.items = tide_day_record.split(",")
        if len(self.items) != 5:
            raise ValueError(f"Expecting 5 items in the tide record, but got {len(self.items)}")
        if 0 < month > 12:
            raise ValueError(f"{month} is not a valid month")
        if tide_type not in ("low", "high"):
            raise ValueError(f"Tide type should be low or high, not {tide_type}")
        
        for i in range(1,5):
            current_field = str.strip(self.items[i])
            if not self.parse_int(current_field):
                raise ValueError(f"Tide data must be expressed as an integer, not: {current_field}")
            if not len(current_field) == 7 and not current_field == '9':
                raise ValueError(f"Each data thing must be 7 digits long, or be '9', representing 'no tide for this time'. Got [{current_field}]")
            self.tide_times.append(current_field)
            
        self.tide_date = (int) (self.items[0])
        self.tide_month = (int) (month)
        self.tide_year = (int) (year)
        self.tide_type = tide_type

    def GetFormattedDay(self):
        """
        Return a record for a tide day that is ready to be plugged into the expected format in the tides 
        spreadsheet. 
        Params:
        tide_times - an array of the 4 tides in a day.
        Full example of the returned record:
        "01/06/2022,3.15,Low,02:29:00,0.54,High,08:31:00,3.51,Low,14:43:00,0.6,High,20:41:00,3.69"
        """
        
        formatted_date = "{:02d}/{:02d}/{:02d}".format(self.tide_date, self.tide_month, self.tide_year)
        tidal_range = Utilities().get_tidal_range2(self.tide_times)
        formatted_record = f"{formatted_date},{tidal_range}"
        for index,i in enumerate(self.tide_times):
            tide_type_asbool = True if self.tide_type == 'High' else False
            formatted_record += Utilities().get_tide_instance2(index, tide_type_asbool, i)
            
        return formatted_record

# Utilities...
        # if an int, return True. Else false
    def parse_int(self, candidate_int):
        try:
            dummy_int = int(candidate_int)
        except ValueError:
            return False
        return True 

