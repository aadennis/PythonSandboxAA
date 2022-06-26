"""
A manager for tide details for a given day in a month.
tide_day_record (passed to ctr) breaks down thus:
Field 1 - date in month
Field 2,3,4,5 - each of these is 7 digits in two sections:
1.time of day: 4 digits, e.g. 0134 = 01h34m
2.tide height: 3 digits, e.g. 113 = 1.13 metres;
"""
class TideDay:

    items = None
    tide_date = None
    tide_month = None
    tide_times = []
    

    def __init__(self, tide_day_record, month, first_tide_type):
        self.validate_record(tide_day_record, month)
        
    # validate the data passed to the constructor.
    # If validation passes, store the data in the object.
    # Else throw exceptions at the first validation error met.
    def validate_record(self, tide_day_record, month):
        self.items = tide_day_record.split(",")
        if len(self.items) != 5:
            raise ValueError(f"Expecting 5 items in the tide record, but got {len(self.items)}")
        if 0 < month > 12:
            raise ValueError(f"{month} is not a valid month")
        for i in range(1,5):
            if not self.parse_int(self.items[i]):
                raise ValueError(f"Tide data is not valid: {self.items[i]}")
            self.tide_times.append(self.items[i])
            
        self.tide_date = (int) (self.items[0])
        self.tide_month = (int) (month)

# Utilities...
        # if an int, return True. Else false
    def parse_int(self, candidate_int):
        try:
            dummy_int = int(candidate_int)
        except ValueError:
            return False
        return True 

