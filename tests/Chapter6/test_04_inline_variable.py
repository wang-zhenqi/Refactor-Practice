from Chapter6.m04_inline_variable import generate_greeting


def test_generate_greeting():
    assert generate_greeting("John", "4", "Ohio") == "Hello! Name: John, Age: 4, City: Ohio"
