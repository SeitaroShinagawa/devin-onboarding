import pytest
from datetime import date

from src.utils import convert_date_string


def test_convert_date_string_valid():
    """Tests that valid date strings are correctly converted."""
    test_cases = [
        ("2025-05-07", date(2025, 5, 7)),
        ("2023-01-01", date(2023, 1, 1)),
        ("2024-12-31", date(2024, 12, 31)),
    ]
    
    for date_string, expected in test_cases:
        assert convert_date_string(date_string) == expected


def test_convert_date_string_invalid():
    """Tests that ValueError is raised for invalid date strings."""
    invalid_dates = [
        "2025/05/07",  # Invalid separator
        "25-5-7",      # Invalid digit count
        "abcd-ef-gh",  # Not numeric
        "",            # Empty string
        "2023-13-01",  # Invalid month
        "2023-02-30",  # Invalid day
    ]
    
    for invalid_date in invalid_dates:
        with pytest.raises(ValueError):
            convert_date_string(invalid_date)
