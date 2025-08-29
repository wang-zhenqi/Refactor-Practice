from Chapter6.m02_inline_function import print_invoice, print_order_summary


def test_print_invoice():
    assert print_invoice(2, 10) == 20


def test_print_order_summary():
    assert print_order_summary("books", 100, 5, 0.8) == 100.0
