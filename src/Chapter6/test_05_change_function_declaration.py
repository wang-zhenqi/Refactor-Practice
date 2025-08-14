from m05_change_function_declaration import calculate_total_price

from Chapter6.m05_change_function_declaration import apply_discount_and_tax


def test_calc_total_price():
    items = [
        {
            "price": 10,
            "quantity": 5,
        },
        {
            "price": 20,
            "quantity": 2,
        },
    ]
    assert calculate_total_price(items) == 90


def test_apply_discount():
    assert apply_discount_and_tax(0.2, 88) == 70.4
    assert apply_discount_and_tax(0.3, 90, 0.1) == 69.3
