import time

# class to be mocked
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        # assume takes a while to get the details...
        time.sleep(3)
        return f"The name of this person is [{self.name}]"

# function under test
def make_person(name):
    person = Person(name)
    return person.get_name()


