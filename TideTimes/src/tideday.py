"""
A manager for tide details for a given day in a month
"""
class TideDay:

    items = None
    tide_date = None
    tide_times = []
    

    def __init__(self, tide_day_record, month, first_tide_type):
        #date_in_month, tide_1, tide_2, tide_3, tide_4):
        self.validate_record(tide_day_record, month)
        # self.date_in_month = date_in_month,
        # self.tide_1 = tide_1,
        # self.tide_2 = tide_2,
        # self.tide_3 = tide_3,
        # self.tide_4 = tide_4    
        
    # if an int, return True. Else false
    def parse_int(self, candidate_int):
        try:
            dummy_int = int(candidate_int)
        except ValueError:
            return False
        return True 

    def validate_record(self, tide_day_record, month):
        self.items = tide_day_record.split(",")
        if len(self.items) != 5:
            raise ValueError(f"Expecting stuff bud, but got {len(self.items)}")
        if 0 < month > 12:
            raise ValueError(f"{month} is not a valid month")
        for i in range(1,5):
            if not self.parse_int(self.items[i]):
                raise ValueError(f"Tide data is not valid: {self.items[i]}")
            self.tide_times.append(self.items[i])
            
        self.tide_date = (int) (self.items[0])
       
        

    def get_items(self):
        return self.tide_date