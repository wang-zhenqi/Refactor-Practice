from typing import Callable


class BloodPressureReading:
    def __init__(self, systolic: int, diastolic: int):
        self.systolic = systolic
        self.diastolic = diastolic


def is_hypertensive(reading: BloodPressureReading) -> bool:
    return reading.systolic >= 140 or reading.diastolic >= 90


def is_prehypertensive(reading: BloodPressureReading) -> bool:
    return 120 <= reading.systolic < 140 or 80 <= reading.diastolic < 90


def categorize_blood_pressure(systolic: int, diastolic: int) -> str:
    reading = BloodPressureReading(systolic, diastolic)
    """分类血压状态"""
    if is_hypertensive(reading):
        return "高血压"
    elif is_prehypertensive(reading):
        return "高血压前期"
    else:
        return "正常"


def log_reading(patient_id: str, systolic: int, diastolic: int, timestamp: str) -> None:
    """记录血压读数"""
    category = categorize_blood_pressure(systolic, diastolic)
    print(f"患者 {patient_id} 在 {timestamp} 的血压: {systolic}/{diastolic} mmHg，状态: {category}")
    alert_if_critical(systolic, diastolic, print)


def alert_if_critical(systolic: int, diastolic: int, callback: Callable[[str], None]) -> None:
    """如果血压危急，触发警报"""
    if systolic >= 180 or diastolic >= 120:
        callback(f"危急！血压过高：{systolic}/{diastolic}")
