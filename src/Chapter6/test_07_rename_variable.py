from m07_rename_variable import check_stock


def test_check_stock():
    actual = check_stock(120)
    assert actual["result"] == "Low Stock Warning"
    assert actual["flag"] is True
