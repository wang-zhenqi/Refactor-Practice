from Chapter6.m07_rename_variable import check_stock


def test_check_stock_given_order_quantity_should_suggest_low_stock_when_remaining_less_then_50():
    actual = check_stock(120)
    assert actual["stock_status_message"] == "Low Stock Warning"
    assert actual["is_low_stock"] is True


def test_check_stock_given_order_quantity_should_suggest_ok_when_remaining_no_less_then_50():
    actual = check_stock(10)
    assert actual["stock_status_message"] == "Stock OK"
    assert actual["is_low_stock"] is False
