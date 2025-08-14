from m05_change_function_declaration import calc_total_price


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
    assert calc_total_price(items) == 90
