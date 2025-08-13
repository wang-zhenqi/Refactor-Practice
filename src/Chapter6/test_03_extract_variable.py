from m03_extract_variable import calculate_total_cost


def test_total_cost():
    assert calculate_total_cost(200, 3, 0.12, 0.2) == 537.6
