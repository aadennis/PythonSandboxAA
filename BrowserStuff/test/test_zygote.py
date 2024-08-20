from aardvark import TrollSaver


class TestTrollSaver():

    def test_build_description(self):
        expected_result = "Age: 312, Hair Color: fuzzy red"
        age = 312
        hair_color = "fuzzy red"
        ts = TrollSaver(age, hair_color)
        description = ts.build_description()
        print(description)
        assert (description == expected_result)
