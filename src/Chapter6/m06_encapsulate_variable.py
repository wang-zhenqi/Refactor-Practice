# 全局变量：默认公司信息
default_company = {
    "name": "TechCorp",
    "country": "USA",
    "founded": 1995,
}


def create_employee(name, age):
    """创建员工信息，关联默认公司"""
    return {
        "name": name,
        "age": age,
        "company": default_company,  # 直接引用全局变量
    }


def get_company_slogan():
    """根据公司信息生成口号"""
    if default_company["country"] == "USA":
        return f"Made in {default_company['country']} with pride!"
    else:
        return f"Global innovation from {default_company['country']}!"


def transfer_company(new_name, new_country):
    """转移公司"""
    global default_company
    default_company = {"name": new_name, "country": new_country, "founded": 1995}  # 直接修改
