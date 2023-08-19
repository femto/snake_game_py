import pytest
from solution import reverse_string

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "olleh"),
        ("OpenAI", "IANepO"),
        ("", ""),
        ("a", "a"),
        ("!@#$%^", "^%$#@!"),
    ]
)
def test_reverse_string(input_string, expected_output):
    assert reverse_string(input_string) == expected_output
