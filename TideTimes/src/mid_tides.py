class TidesForDay():
    """
    Encapsulate tide data for 1 day
    """

    def __init__(self, current_date, tide_day, month_year):
        self.current_date = current_date
        self.tide_day = tide_day
        self.month_year = month_year
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
        """
        return f"{tide_time[0:2]}:{tide_time[2:4]}:00"
        

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

    def format_tide_dictation(input_text, month_year):
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
            tide_days.append(TidesForDay(current_date + 1, tide_day, month_year))
            current_date += 1

        formatted_tide_month = []
        for tide_day in tide_days:
            formatted_tide_month.append(f"{tide_day.print()}")
            
        return formatted_tide_month

    test_text_1 = """
    100533155809 bravo 103431162811 bravo 111529170912 bravo 121427181214 bravo 
    070914133227 bravo 084713150928 bravo 100710163231 bravo 111407173634 bravo 
    121404183237 bravo 065141130902 bravo 073843195700 bravo  
    082344143600 bravo 090543151300 bravo 094542154702 bravo 102239162104 bravo 
    105935165608 bravo 114130173711 bravo 060212124826 bravo 073114142725 bravo 
    093913155026 bravo 104911165529 bravo 114108174531 bravo 122606182834 bravo 
    064037130604 bravo 071538134104 bravo 074738140804 bravo 081738143005 bravo 
    084637144805 bravo 091235150606 bravo
    """

    output_text = format_tide_dictation(test_text_1, "02/2024")
    print(output_text)
