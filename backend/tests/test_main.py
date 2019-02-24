import pytest

from backend.main import clean_text


@pytest.mark.parametrize('text,expected', [
    ('test string', 'test string'),
    ('Test String', 'Test String'),
    (' test string ', 'test string'),
    ('test string!', 'test string'),
    ('test  string', 'test string'),
    ('test $  string', 'test string'),
])
def test_clean_text(text, expected):
    assert clean_text(text) == expected
