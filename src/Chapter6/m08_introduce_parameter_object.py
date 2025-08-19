class BloodPressure:
    def __init__(self, systolic: int, diastolic: int):
        self.systolic = systolic
        self.diastolic = diastolic

    def _is_hypertensive(self):
        return self.systolic >= 140 or self.diastolic >= 90

    def _is_prehypertensive(self):
        return 120 <= self.systolic < 140 or 80 <= self.diastolic < 90

    def categorize(self):
        """分类血压状态"""
        if self._is_hypertensive():
            return "高血压"
        elif self._is_prehypertensive():
            return "高血压前期"
        else:
            return "正常"


class BloodPressureReading:
    def __init__(self, patient_id: str, bp: BloodPressure, ts: str):
        self.patient_id = patient_id
        self.blood_pressure = bp
        self.timestamp = ts

    def report(self) -> str:
        return (
            f"患者 {self.patient_id} 在 {self.timestamp} 的血压："
            f"{self.blood_pressure.systolic}/{self.blood_pressure.diastolic} mmHg，"
            f"状态：{self.blood_pressure.categorize()}"
        )
