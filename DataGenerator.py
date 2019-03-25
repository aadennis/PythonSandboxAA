# Create fake test data

import random
import datetime
from datetime import timedelta
import string

def get_standardised_date():
    return datetime.date(1970,1,1) + timedelta(days = random.randint(1,3600))

def get_firstuse_date():
    return datetime.date(1940,1,1) + timedelta(days = random.randint(1,3600))

def get_deprecation_date(OpenDate):
    close_date = OpenDate + timedelta(days = random.randint(1,15000))
    today = datetime.datetime.today().date()
    if close_date > today:
        close_date = today
    return close_date
    
def build_dictionaryEntry_standard(SourceWord):
    word_types = ["VERB","NOUN"]
    status_types = ["ACTIVE","DEPRECATED"]
    language_types = ["LANGUAGE","DIALECT"]
    open_date = get_standardised_date()
    close_date = get_deprecation_date(open_date)

    word = "INDEX/{0}".format(SourceWord)

    tempStr = "{0:30}".format(word)
    tempStr += "{0:12}".format(random.choice(word_types))
    tempStr += "{0:10}".format(open_date.strftime("%Y%m%d000000"))
    tempStr += "{0:10}".format(close_date.strftime("%Y%m%d000000"))
    tempStr += "{0:3}".format("")
    tempStr += "{0:12}".format(random.choice(status_types))
    tempStr += "{0:12}".format(random.choice(language_types))
    tempStr += "{0:1}".format("S")
    tempStr += "\n"
    return tempStr

def make_fake_dictionary_file(number_of_words, file_name):
    with open(file_name, "w") as dictionary_file:
        for i in range(1, number_of_words + 1):
            wordRecord = build_dictionaryEntry_standard(i)
            dictionary_file.write(wordRecord)


    
    
    

# entry point
make_fake_dictionary_file(50,"FrenchDictionary.dic")


