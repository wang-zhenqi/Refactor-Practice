from m05_change_function_declaration import calculate_total_price


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
