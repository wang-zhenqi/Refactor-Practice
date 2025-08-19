import pytest
from m08_introduce_parameter_object import categorize_blood_pressure


@pytest.mark.parametrize(
    "systolic,diastolic,expected",
    [
        (145, 89, "高血压"),
        (119, 82, "高血压前期"),
        (116, 79, "正常"),
    ],
)
def test_categorize_blood_pressure(systolic, diastolic, expected):
    assert categorize_blood_pressure(systolic, diastolic) == expected
