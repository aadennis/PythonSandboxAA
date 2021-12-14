from unittest.mock import patch
from GistTypes.src.Patch.Set5.Person import Person

def test_get_person():
    MOCK_SSN = "102102102X"

    with patch.object(Person, 'get_ssn', return_value = MOCK_SSN):
        p = Person("Brown", "Jimmy")
        name_as_sentence = p.get_details()
        assert name_as_sentence == f"ssn: {MOCK_SSN}/full name:The name of this person is [Jimmy][Brown]"

test_get_person()

