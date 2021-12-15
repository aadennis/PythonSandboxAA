from unittest.mock import patch
from GistTypes.src.Patch.Set3.Person import Person, make_person

def test_make_person():
    MOCK_NAME_AS_SENTENCE = "replaced by the mock"
    with patch.object(Person, 'get_name', return_value = MOCK_NAME_AS_SENTENCE):
        name_as_sentence = make_person("Harry")
        print(name_as_sentence)
        assert name_as_sentence == MOCK_NAME_AS_SENTENCE


test_make_person()

