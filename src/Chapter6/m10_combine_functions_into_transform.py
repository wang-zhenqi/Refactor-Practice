from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    base_salary: float
    years_of_service: int


class EnrichedEmployee(Employee):
    total_compensation: float
    after_tax_salary: float
    seniority_bonus: float


class CompensationReport(BaseModel):
    name: str
    base_salary: float
    seniority_bonus: float
    after_tax_salary: float
    total_compensation: float

    @classmethod
    def from_enriched(cls, employee: EnrichedEmployee) -> "CompensationReport":
        return cls(
            name=employee.name,
            base_salary=employee.base_salary,
            seniority_bonus=employee.seniority_bonus,
            after_tax_salary=employee.after_tax_salary,
            total_compensation=employee.total_compensation,
        )


def enrich_employee_record(employee: Employee) -> EnrichedEmployee:
    _bonus = employee.years_of_service * 1000
    return EnrichedEmployee(
        name=employee.name,
        base_salary=employee.base_salary,
        years_of_service=employee.years_of_service,
        total_compensation=employee.base_salary + _bonus,
        after_tax_salary=employee.base_salary * 0.8,
        seniority_bonus=_bonus,
    )


def create_compensation_report(employees: list[Employee]) -> list[dict]:
    enriched_employees = [enrich_employee_record(emp) for emp in employees]
    return [CompensationReport.from_enriched(emp).model_dump() for emp in enriched_employees]
