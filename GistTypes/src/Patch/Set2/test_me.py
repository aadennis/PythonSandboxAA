from unittest.mock import patch
import main

def test_f_a():
    MOCK_RETVAL = 48
    with patch("main.f_b") as f_b_mock:
        # arrange
        f_b_mock.return_value = MOCK_RETVAL
        # act
        ret = main.f_a()
        # assert
        assert main.f_a() == MOCK_RETVAL + 1

test_f_a()

