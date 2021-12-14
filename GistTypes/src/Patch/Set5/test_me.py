# see - https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
from unittest.mock import patch
from GistTypes.src.Patch.Set5.Person import Person

def test_get_person():
    MOCK_SSN = "102102102X"

    with patch.object(Person, 'get_ssn', return_value = MOCK_SSN) as mock_get_ssn:
        p = Person("Brown", "Jimmy")
        name_as_sentence = p.get_details()
        assert name_as_sentence == \
        f"ssn: {MOCK_SSN}/full name:The name of this person is [Jimmy][Brown]"
        mock_get_ssn.assert_called_once()
        # same as...
        count = mock_get_ssn.call_count
        assert count == 1

test_get_person()

