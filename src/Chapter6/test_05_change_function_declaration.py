from m05_change_function_declaration import apply_discount, calculate_total_price


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
    assert apply_discount(88, 0.2) == 70.4
