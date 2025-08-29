from Chapter6.m10_combine_functions_into_transform import (
    create_compensation_report,
    enrich_employee_record,
)


def test_create_compensation_report():
    employees = [
        {"name": "Alice", "base_salary": 8000, "years_of_service": 5},
        {"name": "Bob", "base_salary": 10000, "years_of_service": 8},
        {"name": "Charlie", "base_salary": 12000, "years_of_service": 10},
    ]

    expected = [
        {
            "name": "Alice",
            "base_salary": 8000,
            "seniority_bonus": 5000,
            "after_tax_salary": 6400.0,
            "total_compensation": 13000,
        },
        {
            "name": "Bob",
            "base_salary": 10000,
            "seniority_bonus": 8000,
            "after_tax_salary": 8000.0,
            "total_compensation": 18000,
        },
        {
            "name": "Charlie",
            "base_salary": 12000,
            "seniority_bonus": 10000,
            "after_tax_salary": 9600.0,
            "total_compensation": 22000,
        },
    ]
    assert create_compensation_report(employees) == expected


def test_given_employee_record_when_enrich_then_original_data_should_not_change():
    employee = {"name": "Alice", "base_salary": 8000, "years_of_service": 5}
    enriched_employee = enrich_employee_record(employee)

    assert enriched_employee["name"] == "Alice"
    assert enriched_employee["base_salary"] == 8000
    assert enriched_employee["years_of_service"] == 5
    assert employee is not enriched_employee


def test_given_employee_record_when_enrich_then_enriched_data_should_have_derived_fields():
    employee = {"name": "Alice", "base_salary": 8000, "years_of_service": 5}
    enriched_employee = enrich_employee_record(employee)

    assert enriched_employee["total_compensation"] == 13000
    assert enriched_employee["after_tax_salary"] == 6400.0
    assert enriched_employee["seniority_bonus"] == 5000
