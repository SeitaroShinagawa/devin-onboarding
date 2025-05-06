import pytest
from datetime import date

from src.utils import convert_date_string


def test_convert_date_string_valid():
    """有効な日付文字列が正しく変換されることをテストします。"""
    test_cases = [
        ("2025-05-07", date(2025, 5, 7)),
        ("2023-01-01", date(2023, 1, 1)),
        ("2024-12-31", date(2024, 12, 31)),
    ]
    
    for date_string, expected in test_cases:
        assert convert_date_string(date_string) == expected


def test_convert_date_string_invalid():
    """無効な日付文字列でValueErrorが発生することをテストします。"""
    invalid_dates = [
        "2025/05/07",  # 不正なセパレータ
        "25-5-7",      # 不正な桁数
        "abcd-ef-gh",  # 数字ではない
        "",            # 空文字列
        "2023-13-01",  # 不正な月
        "2023-02-30",  # 不正な日
    ]
    
    for invalid_date in invalid_dates:
        with pytest.raises(ValueError):
            convert_date_string(invalid_date)
