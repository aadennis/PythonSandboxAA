"""
A manager for tide details for a given day in a month
"""
class TideDay:

    items = None
    tide_date = None
    

    def __init__(self, tide_day_record, month, first_tide_type):
        #date_in_month, tide_1, tide_2, tide_3, tide_4):
        self.validate_record(tide_day_record, month)
        # self.date_in_month = date_in_month,
        # self.tide_1 = tide_1,
        # self.tide_2 = tide_2,
        # self.tide_3 = tide_3,
        # self.tide_4 = tide_4     

    def validate_record(self, tide_day_record, month):
        self.items = tide_day_record.split(",")
        if len(self.items) != 5:
            raise ValueError(f"Expecting stuff bud, but got {len(self.items)}")
        if 0 < month > 12:
            raise ValueError(f"{month} is not a valid month")
        self.tide_date = (int) (self.items[0])
        

    def get_items(self):
        return self.tide_date