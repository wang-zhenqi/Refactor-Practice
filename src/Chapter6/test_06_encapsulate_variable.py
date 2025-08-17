from m06_encapsulate_variable import (
    create_employee,
    get_company_slogan,
    transfer_company,
)


def test_create_employee():
    create_employee("Alice", 30)
    assert "Made in USA with pride!" == get_company_slogan()


def test_transfer_company():
    transfer_company("NewWorld Inc", "Canada")
    assert "Global innovation from Canada!" == get_company_slogan()
