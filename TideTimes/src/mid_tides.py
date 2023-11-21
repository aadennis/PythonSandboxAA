class TideDay():
    """
    Encapsulate tide data for 1 day
    """

    def __init__(self, current_date, tide_day, month_year):
        self.current_date = current_date 
        self.tide_day = tide_day
        self.month_year = month_year
        self.formatted_date = self.format_date()
        self.tide_time_1 = tide_day[0:4]
        self.tide_height_1 = tide_day[4:6]
        self.tide_time_2 = tide_day[6:10]
        self.tide_height_2 = tide_day[10:12]
        self.formatted_tide_time_1 = self.format_tide_time(self.tide_time_1)
        self.formatted_tide_time_2 = f"{self.tide_time_2[0:2]}:{self.tide_time_2[2:4]}:00"
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
        return f"{tide_time[0:2]}:{tide_time[2:4]}:00"
        

    def format_date(self):
        """
        Given say "31" and "12/2023", cat and return "31/12/2023"
        """
        return f"{str(self.current_date).zfill(2)}/{self.month_year}"
            
    def print(self):
        formatted_tide_day = f"{self.format_date()},{self.tidal_range},{self.tide_1_type},{self.formatted_tide_time_1},{self.formatted_tide_height_1},{self.tide_2_type},{self.formatted_tide_time_2},{self.formatted_tide_height_2}"
        return formatted_tide_day

def get_other_tide(current_tide):
    if current_tide == 'High':
        return 'Low'
    return 'High'

def format_tide_dictation(input_text, month_year):
    """
        input_text is the tide table as dictated. 
        month_year is e.g. "12/2023" - note the format. It is mandatory. The date
        of the month is then inferred, and the whole pasted together.
        Context: In any one calendar day, there are only 2 usable high/low waters 
        (HLWs), give or take, which are the middle 2 of 4. If there are 3 HLWs, then 
        dictate the first 2 of 3. This happens when the first tide of the calendar 
        day swaps from being a high to a low or vice-versa.
        The use of Bravo is because SpeechToText (STT) engines routinely
        fail to hear "new line", or at least, to understand that it is not a literal
        . For this, the code ignores it, and uses the token separator of space to replace with newline.
        An example of input, taken from (flawed) output from dictation, is below 
        in test_text_1. test_text_2 is good dictation.
        An example of how the final output should look for a single day:

        30/11/2023,3.3,Low,01:58:00,0.6,High,07:58:00,3.9

        The second value is the tidal range. This is an approximation, as not all 4 
        values for the day are available from the dictation, just 2. But good enough
        for the requirement. 
    """    


    words = input_text.lower().split()
    tide_days = []


    current_date = 0
    for i, tide_day in enumerate(words):
        if tide_day == 'bravo': # ignore - just visual punctuation for the dictator
            continue
        else:
            # must be data for a day, e.g. 091512153518 meaning:
            # first (usable) tide is 09:15 with height 1.2 metres
            # second tide is 15:35 with height 1.8 metres
            
            #translated_words.append(f"{formatted_date},{tide_type_1},{tide_1},{tide_type_2},{tide_2}")
            tide_days.append(TideDay(current_date + 1, tide_day, month_year))
            current_date += 1

    formatted_tide_month = ""
    for tide_day in tide_days:
        formatted_tide_month += f"{tide_day.print()}\n"
        

    #translated_text = ' '.join(translated_words).replace(' ','\n')
    return formatted_tide_month

test_text_1 = """
 Lima 082838145008 bravo 085936152210 bravo 093534155672
 bravo 2B101731163813B110930173014B 121229183114 bravo hotel 070115132329 
 bravo 081214143430 bravo 091512153532 bravo 101110163134 bravo 110108172235 
 bravo hotel 110236170809 bravo"""

test_text_2 = """
Hotel 082838145008 bravo 085936152210 bravo 093534155612 bravo
 101731163813 bravo 110930173014 bravo Lima 055015121229 bravo
   070115132329 bravo 081214143430 bravo 091512153532 bravo 
   101010163134 bravo 110108172235 bravo Hotel 054837114907 bravo 
   063439123806 bravo 071640132405 bravo 075640140805 bravo 083840144906 
   bravo 092339153206 bravo 101137161808 bravo 110236170809 bravo Lima 
   052711120034 bravo 063011130433 bravo 074911141433 bravo 090410152233 bravo 
   101009162534 bravo 110808172235 bravo hotel 054637120007 bravo 063238124706 
   bravo 071239133106 bravo 074638140807 bravo 081838144007 
   bravo 085137151008 bravo"""

test_text_3 = """
082838145008 bravo 085936152210 bravo 093534155612 bravo
 101731163813 bravo 110930173014 bravo 055015121229 bravo
   070115132329 bravo 081214143430 bravo 091512153532 bravo 
   101010163134 bravo 110108172235 bravo 054837114907 bravo 
   063439123806 bravo 071640132405 bravo 075640140805 bravo 083840144906 
   bravo 092339153206 bravo 101137161808 bravo 110236170809 bravo 
   052711120034 bravo 063011130433 bravo 074911141433 bravo 090410152233 bravo 
   101009162534 bravo 110808172235 bravo 054637120007 bravo 063238124706 
   bravo 071239133106 bravo 074638140807 bravo 081838144007 
   bravo 085137151008 bravo"""

output_text = format_tide_dictation(test_text_3, "12/2023")
print(output_text)
