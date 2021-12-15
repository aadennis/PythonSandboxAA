from unittest.mock import patch
import GistTypes.src.Patch.Set2.main as main

def test_f_a():
    MOCK_RETVAL = 48
    with patch('GistTypes.src.Patch.Set2.main.f_b') as f_b_mock:
        # arrange
        f_b_mock.return_value = MOCK_RETVAL
        # act
        ret = main.f_a()
        print(f"\nret: {ret}")
        print(f"MOCK_RETVAL: {MOCK_RETVAL}")
        # assert
        assert main.f_a() == MOCK_RETVAL + 1

test_f_a()

