from production_plan.province import Province


def test_province_should_calculate_shortfall(asia):
    assert asia.shortfall() == 5


def test_province_should_calculate_profit(asia):
    assert asia.profit() == 230


def test_something(asia):
    asia.producers[0].set_production(20)
    assert asia.shortfall() == -6
    assert asia.profit() == 292


def test_no_producers():
    data = {"name": "No producers", "producers": [], "demand": 30, "price": 20}
    no_producers = Province(data)
    assert no_producers.shortfall() == 30
    assert no_producers.profit() == 0


def test_zero_demand():
    data = {"name": "Zero demand", "producers": [{"name": "zero", "cost": 1, "production": 0}], "demand": 0, "price": 1}
    zero_demand = Province(data)
    assert zero_demand.shortfall() == 0
    assert zero_demand.profit() == 0


def test_negative_demand():
    data = {
        "name": "Negative demand",
        "producers": [{"name": "negative", "cost": 1, "production": 0}],
        "demand": -1,
        "price": 1,
    }
    negative_demand = Province(data)
    assert negative_demand.shortfall() == -1
    assert negative_demand.profit() == 0


def test_empty_string_demand():
    data = {
        "name": "Empty string demand",
        "producers": [{"name": "empty string", "cost": 1, "production": 0}],
        "demand": "",
        "price": 1,
    }
    empty_string_demand = Province(data)
    assert empty_string_demand.shortfall() == 0
    assert empty_string_demand.profit() == 0


def test_string_for_producers():
    data = {
        "name": "String for producers",
        "producers": "string",
        "demand": 30,
        "price": 20,
    }
    string_for_producers = Province(data)
    assert string_for_producers.shortfall() == 30
    assert string_for_producers.profit() == 0
