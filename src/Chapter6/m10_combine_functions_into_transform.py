from copy import deepcopy


def calculate_seniority_bonus(employee):
    return employee["years_of_service"] * 1000


def calculate_after_tax_salary(employee):
    return employee["base_salary"] * 0.8


def calculate_total_compensation(employee):
    bonus = calculate_seniority_bonus(employee)
    return employee["base_salary"] + bonus


def enhance_the_employee_record(employee):
    return deepcopy(employee)


def create_compensation_report(employees):
    result = []
    for emp in employees:
        report_item = {
            "name": emp["name"],
            "base_salary": emp["base_salary"],
            "seniority_bonus": calculate_seniority_bonus(emp),
            "after_tax_salary": calculate_after_tax_salary(emp),
            "total_compensation": calculate_total_compensation(emp),
        }
        result.append(report_item)
    return result
