def process_student_grades(student):
    # 计算总分
    total_score = sum_total_score(student)

    # 计算平均分
    average_score = total_score / len(student["grades"])

    # 判断是否及格
    if average_score >= 60:
        status = "Pass"
    else:
        status = "Fail"

    # 生成成绩报告
    report = {"name": student["name"], "total_score": total_score, "average_score": average_score, "status": status}

    return report


def sum_total_score(student):
    total_score = 0
    for subject, score in student["grades"].items():
        total_score += score
    return total_score


# 示例学生数据
alice = {"name": "Alice", "grades": {"Math": 85, "Science": 90, "History": 75, "English": 80}}

print(process_student_grades(alice))
