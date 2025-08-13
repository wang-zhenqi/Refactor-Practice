from m02_inline_function import print_invoice


def test_print_invoice():
    quantity = 2
    price = 10
    expected = 20
    assert print_invoice(quantity, price) == expected
