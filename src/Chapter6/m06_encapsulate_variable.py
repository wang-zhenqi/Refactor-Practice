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


"""
勘误：上次提交（23698343, "init the code and tests"）中的测试样例写得不对。
应该像现在这样，测试代码中调用 `create_employee` 和 `transfer_company`，然后通过 `get_company_slogan`
来验证 slogan 是否正确。

原则：对于所有可变的数据，只要它的作用域超出单个函数，就将其封装起来，只允许通过函数访问。数据的作用域越大，封装就越重要。

重构步骤：
1. 为变量的读取和修改编写函数
2. 逐步利用测试将所有的变量替换为该函数
3. 修改原始变量的可见性或者改名（这样可以避免遗漏——如果有遗漏就一定会报错；还可保证之后的代码不会直接访问该变量）
"""
