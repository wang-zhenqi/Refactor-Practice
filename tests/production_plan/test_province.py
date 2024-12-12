from production_plan.province import Province


def test_province_should_calculate_shortfall(sample_province_data):
    asia = Province(sample_province_data)
    assert asia.shortfall() == 5
