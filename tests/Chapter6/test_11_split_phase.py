from src.Chapter6.m11_split_phase import calculate_discount


def test_calculate_discount():
    raw_data = "premium, 2000.00, electronics"
    assert calculate_discount(raw_data) == 400.0
