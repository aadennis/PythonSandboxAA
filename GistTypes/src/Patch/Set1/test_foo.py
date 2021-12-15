# run as [python3 test_foo.py]
from unittest.mock import patch
from my_module import f_a


def test_f_a():
    with patch("db.db_write") as db_write:
        db_write.return_value = 33
        assert f_a() == 343

test_f_a()
