def process_student_grades(student: dict) -> dict:
    # 计算总分
    total_score = sum_total_score(student["grades"])

    # 计算平均分
    average_score = cal_average(total_score, len(student["grades"]))

    # 判断是否及格
    status = determine_status(average_score)

    # 生成成绩报告
    return generate_report(
        student["name"],
        total_score,
        average_score,
        status,
    )


def generate_report(student_name: str, total_score: float, average_score: float, status: str) -> dict:
    return {
        "name": student_name,
        "total_score": total_score,
        "average_score": average_score,
        "status": status,
    }


def determine_status(average_score: float) -> str:
    return "Pass" if average_score >= 60 else "Fail"


def cal_average(total_score: float, num_subject: int) -> float:
    return total_score / num_subject


def sum_total_score(grades: dict[str, float]) -> float:
    return sum(grades.values())


# 示例学生数据
alice = {"name": "Alice", "grades": {"Math": 85, "Science": 90, "History": 75, "English": 80}}

print(process_student_grades(alice))
