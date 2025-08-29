from copy import deepcopy


def enrich_the_employee_record(employee):
    enriched_employee = deepcopy(employee)

    _seniority_bonus = employee["years_of_service"] * 1000
    enriched_employee["total_compensation"] = employee["base_salary"] + _seniority_bonus
    enriched_employee["after_tax_salary"] = employee["base_salary"] * 0.8
    enriched_employee["seniority_bonus"] = _seniority_bonus

    return enriched_employee


def create_compensation_report(employees):
    result = []
    for emp in employees:
        emp = enrich_the_employee_record(emp)
        report_item = {
            "name": emp["name"],
            "base_salary": emp["base_salary"],
            "seniority_bonus": emp["seniority_bonus"],
            "after_tax_salary": emp["after_tax_salary"],
            "total_compensation": emp["total_compensation"],
        }
        result.append(report_item)
    return result
