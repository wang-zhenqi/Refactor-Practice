def process_student_grades(student):
    # 计算总分
    total_score = 0
    for subject, score in student["grades"].items():
        total_score += score

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


# 示例学生数据
student = {"name": "Alice", "grades": {"Math": 85, "Science": 90, "History": 75, "English": 80}}

print(process_student_grades(student))
