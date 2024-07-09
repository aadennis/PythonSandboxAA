class TidesForDay():
    """
    Encapsulate tide data for 1 day
    """

    def __init__(self, current_date, tide_day, month_year, Is_BST=False):
        self.current_date = current_date
        self.tide_day = tide_day
        self.month_year = month_year
        self.Is_BST = Is_BST 
        self.format_tide(tide_day)

    def format_tide(self, tide_day):
        """
        Convert the raw digits in tide_day to a readable format
        """
        self.formatted_date = self.format_date()
        self.tide_time_1 = tide_day[0:4]
        self.tide_height_1 = tide_day[4:6]
        self.tide_time_2 = tide_day[6:10]
        self.tide_height_2 = tide_day[10:12]
        self.formatted_tide_time_1 = self.format_tide_time(self.tide_time_1)
        self.formatted_tide_time_2 = self.format_tide_time(self.tide_time_2)
        self.formatted_tide_height_1 = int(self.tide_height_1) / 10
        self.formatted_tide_height_2 = int(self.tide_height_2) / 10
        if (self.formatted_tide_height_1 > self.formatted_tide_height_2):
            self.tide_1_type = "High"
            self.tide_2_type = "Low"
        else:
            self.tide_1_type = "Low"
            self.tide_2_type = "High"
        self.tidal_range = (abs(int(self.tide_height_1) - int(self.tide_height_2))) / 10

    def format_tide_time(self, tide_time):
        """
        Convert a time value e.g. 0955 to 09:55
        If Is_BST is True, add an hour to the time.
        """
        hour = int(tide_time[0:2])
        if self.Is_BST:
            hour = (hour + 1) % 24  # Add an hour, no need to handle rollover for now
        return f"{str(hour).zfill(2)}:{tide_time[2:4]}:00"
        

    def format_date(self):
        """
        Given say "31" and "12/2023", cat and return "31/12/2023"
        """
        return f"{str(self.current_date).zfill(2)}/{self.month_year}"
            
    def print(self):
        """
        Format the tide day as a single line, CSV.
        """
        formatted_tide_day = f"{self.format_date()},{self.tidal_range},{self.tide_1_type},{self.formatted_tide_time_1},{self.formatted_tide_height_1},{self.tide_2_type},{self.formatted_tide_time_2},{self.formatted_tide_height_2}"
        return formatted_tide_day

# end of class

class TidesForMonth():

    def format_tide_dictation(self, input_text, month_year, Is_BST=False):
        """
            input_text is the tide table as dictated. 
            month_year is e.g. "12/2023" - note the format. It is mandatory. The date
            of the month is then inferred, and the whole pasted together to give eg 09/12/2023
            Context: In any one calendar day, there are only 2 usable high/low waters 
            (HLWs), give or take, which are the middle 2 of 4. If there are 3 HLWs, then 
            dictate the first 2 of 3. This happens when the first tide of the calendar 
            day swaps from being a high to a low or vice-versa.
            The use of Bravo is a substitute for "new line", because SpeechToText (STT) engines
            routinely misinterpret it, or at least, fail to understand that it is not a literal.
            For this, the code ignores it, and uses the token separator of space to replace with newline.
            An example of input, taken from output from dictation, is below 
            in test_text_1. 
            An example of how the final output should look for a single day:

            30/11/2023,3.3,Low,01:58:00,0.6,High,07:58:00,3.9

            The second value is the tidal range. This is an approximation, as not all 4 
            values for the day are available from the dictation, just 2. But good enough
            for the requirement. 
        """    


        words = input_text.lower().split()
        tide_days = []

        current_date = 0
        for _, tide_day in enumerate(words):
            if tide_day == 'bravo': # ignore - just visual punctuation for the dictator
                continue

            # Got here? Must be data for a day, e.g. 091512153518 meaning:
            # first (usable) tide is 09:15 with height 1.2 metres
            # second tide is 15:35 with height 1.8 metres
            tide_days.append(TidesForDay(current_date + 1, tide_day, month_year, Is_BST))
            current_date += 1

        formatted_tide_month = []
        for tide_day in tide_days:
            formatted_tide_month.append(f"{tide_day.print()}")
            
        return '\n'.join(formatted_tide_month)

test_text_1 = """
073609140431 bravo 085209151532 bravo
100108161933 bravo 110407171735 bravo 
054934120106 bravo 064334125206 bravo
072734133806 bravo 080634141606 bravo 
084233144806 bravo 091432151707 bravo
094631154509 bravo 101930161310 bravo
105629164311 bravo 113828172312 bravo
055112129927 bravo 065913133127 bravo 
081612144628 bravo 092611155531 bravo 
102909165535 bravo 052732112908 bravo
062334122506 bravo 071336131704 bravo 
075837140403 bravo 084237144403 bravo 
092537152103 bravo 10536155804  bravo
104635163606 bravo 113033171708 bravo 
054509122230 bravo 064811132829 bravo 
081712144929 bravo
"""

t = TidesForMonth()
output_text = t.format_tide_dictation(test_text_1, "07/2024", True)
print(output_text)
