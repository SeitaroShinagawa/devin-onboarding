from datetime import date
from typing import Optional
import re


def convert_date_string(date_string: str) -> date:
    """Converts a date string to a datetime.date object.
    
    Args:
        date_string (str): The date string to convert. Format must be "YYYY-MM-DD".
            Example: "2025-05-07"
    
    Returns:
        date: The converted date object.
    
    Raises:
        ValueError: If the date string has an invalid format.
    """
    if not date_string or not re.match(r'^\d{4}-\d{2}-\d{2}$', date_string):
        raise ValueError(f"Invalid date format: {date_string}. Expected format: YYYY-MM-DD")
    
    try:
        year, month, day = map(int, date_string.split('-'))
        return date(year, month, day)
    except ValueError:
        raise ValueError(f"Invalid date values: {date_string}. Date does not exist.")
