# 全局变量：默认公司信息
_default_company_data = {
    "name": "TechCorp",
    "country": "USA",
    "founded": 1995,
}


def default_company():
    return _default_company_data


def set_default_company(data):
    global _default_company_data
    _default_company_data = data


def get_company_slogan():
    """根据公司信息生成口号"""
    company = default_company()
    if company["country"] == "USA":
        return f"Made in {company['country']} with pride!"
    else:
        return f"Global innovation from {company['country']}!"


def create_employee(name, age):
    """创建员工信息，关联默认公司"""
    return {
        "name": name,
        "age": age,
        "company": default_company(),  # 直接引用全局变量
    }


def transfer_company(new_name, new_country):
    """转移公司"""
    set_default_company(
        {
            "name": new_name,
            "country": new_country,
            "founded": 1995,
        }
    )
