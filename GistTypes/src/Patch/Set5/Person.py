import time
import random

# class to be mocked
class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def get_name(self):
        # assume takes a while to get the details...
        time.sleep(3)
        full_name = f"The name of this person is [{self.first_name}][{self.last_name}]"
        print(full_name)
        return full_name

    def get_ssn(self):
        ssn = random.randint(11000000,19999999)
        print(ssn)
        return ssn

    def get_details(self):
        this_ssn = self.get_ssn()
        details = f"ssn: {this_ssn}/full name:{self.get_name()}"
        print(details)
        return details


person = Person("Brown","James")
d = person.get_details()
# n = person.get_name()
# s = person.get_ssn()



