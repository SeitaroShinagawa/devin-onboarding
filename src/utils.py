from datetime import date
from typing import Optional
import re


def convert_date_string(date_string: str) -> date:
    """日付文字列をdatetime.dateオブジェクトに変換します。
    
    Args:
        date_string: 変換する日付文字列。フォーマットは"YYYY-MM-DD"である必要があります。
            例: "2025-05-07"
    
    Returns:
        datetime.date型のオブジェクト。
    
    Raises:
        ValueError: 日付文字列が無効な形式の場合に発生します。
    """
    if not date_string or not re.match(r'^\d{4}-\d{2}-\d{2}$', date_string):
        raise ValueError(f"Invalid date format: {date_string}. Expected format: YYYY-MM-DD")
    
    try:
        year, month, day = map(int, date_string.split('-'))
        return date(year, month, day)
    except ValueError:
        raise ValueError(f"Invalid date values: {date_string}. Date does not exist.")
