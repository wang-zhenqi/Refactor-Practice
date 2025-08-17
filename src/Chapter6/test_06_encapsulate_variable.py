from m06_encapsulate_variable import create_employee, transfer_company


def test_create_employee():
    assert {
        "name": "Alice",
        "age": 30,
        "company": {
            "name": "TechCorp",
            "country": "USA",
            "founded": 1995,
        },
    } == create_employee("Alice", 30)


def test_transfer_company():
    transfer_company("NewWorld Inc", "Canada")
