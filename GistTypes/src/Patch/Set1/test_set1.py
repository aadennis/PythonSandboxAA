from unittest.mock import patch
import GistTypes.src.Patch.Set1.my_module as main
#import GistTypes.src.Patch.Set1.db as db


def test_f_a():
    with patch('GistTypes.src.Patch.Set1.my_module.call_db_write') as call_db_write:
        call_db_write.return_value = 33
        assert main.f_a() == 34

test_f_a()
