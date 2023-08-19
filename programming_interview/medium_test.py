import pytest
from solution import longest_substring_length

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdefg", 7),
        ("aab", 2),
        ("abba", 2)
    ]
)
def test_longest_substring_length(input_string, expected_output):
    assert longest_substring_length(input_string) == expected_output
