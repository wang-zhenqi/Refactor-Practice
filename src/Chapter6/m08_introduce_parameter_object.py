class BloodPressureReading:
    def __init__(self, systolic, diastolic):
        self.systolic = systolic
        self.diastolic = diastolic


def is_hypertensive(systolic, diastolic, reading: BloodPressureReading):
    """判断是否为高血压
    :param reading:
    """
    return reading.systolic >= 140 or diastolic >= 90


def is_prehypertensive(systolic, diastolic):
    """判断是否为高血压前期"""
    return 120 <= systolic < 140 or 80 <= diastolic < 90


def categorize_blood_pressure(systolic, diastolic):
    reading = BloodPressureReading(systolic, diastolic)
    """分类血压状态"""
    if is_hypertensive(systolic, diastolic, reading):
        return "高血压"
    elif is_prehypertensive(systolic, diastolic):
        return "高血压前期"
    else:
        return "正常"


def log_reading(patient_id, systolic, diastolic, timestamp):
    """记录血压读数"""
    category = categorize_blood_pressure(systolic, diastolic)
    return f"患者 {patient_id} 在 {timestamp} 的血压: {systolic}/{diastolic} mmHg，状态: {category}"


def alert_if_critical(systolic, diastolic, callback):
    """如果血压危急，触发警报"""
    if systolic >= 180 or diastolic >= 120:
        callback(f"危急！血压过高：{systolic}/{diastolic}")
