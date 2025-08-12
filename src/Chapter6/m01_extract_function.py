def process_student_grades(student):
    # 计算总分
    total_score = sum_total_score(student["grades"])

    # 计算平均分
    average_score = total_score / len(student["grades"])

    # 判断是否及格
    status = determine_status(average_score)

    # 生成成绩报告
    return generate_report(
        student["name"],
        total_score,
        average_score,
        status,
    )


def generate_report(student_name, total_score, average_score, status):
    report = {
        "name": student_name,
        "total_score": total_score,
        "average_score": average_score,
        "status": status,
    }
    return report


def determine_status(average_score):
    return "Pass" if average_score >= 60 else "Fail"


def sum_total_score(grades):
    total_score = 0
    for subject, score in grades.items():
        total_score += score
    return total_score


# 示例学生数据
alice = {"name": "Alice", "grades": {"Math": 85, "Science": 90, "History": 75, "English": 80}}

print(process_student_grades(alice))
