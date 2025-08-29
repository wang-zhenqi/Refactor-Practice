import pytest

from Chapter6.m08_introduce_parameter_object import BloodPressure, BloodPressureReading


@pytest.mark.parametrize(
    "systolic,diastolic,expected",
    [
        (145, 89, "高血压"),
        (119, 82, "高血压前期"),
        (116, 79, "正常"),
    ],
)
def test_categorize_blood_pressure(systolic, diastolic, expected):
    assert BloodPressure(systolic, diastolic).categorize() == expected


def test_reading_report():
    assert (
        "患者 123 在 11223344 的血压：128/89 mmHg，状态：高血压前期"
        == BloodPressureReading("123", BloodPressure(128, 89), "11223344").report()
    )
