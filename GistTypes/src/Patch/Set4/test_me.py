from unittest.mock import Mock
import pytest
import GistTypes.src.Patch.Set4.Image as Image

@pytest.mark.skip(reason="no way of currently testing this")
def test_called():
    mock = Mock()
    mock.some_method = Mock(return_value=None)

    Image.function_with_call(mock, "foo bar")
    assert 1 == 1

    # will return true if method was not called one or more times
    mock.some_method.assert_not_called()




