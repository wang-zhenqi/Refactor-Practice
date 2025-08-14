from m05_change_function_declaration import (
    User,
    apply_discount_and_tax,
    calculate_shipping_cost,
    calculate_total_price,
    calculate_user_score,
)


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


def test_calculate_shipping_cost():
    assert calculate_shipping_cost(10, 100, 0.5, 0.2) == 25
    assert calculate_shipping_cost(10, 199, 0.5, 0.2) == 44.8


def test_calculate_user_score():
    user = User(name="Alice", age=30, email="alice@example.com", activity_level=3, membership_years=5)
    assert calculate_user_score(user.age, user.activity_level) == 360
