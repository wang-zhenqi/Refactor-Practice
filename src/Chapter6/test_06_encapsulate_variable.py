import pytest
from m06_encapsulate_variable import (
    create_employee,
    default_company,
    get_company_slogan,
    set_default_company,
    transfer_company,
)


@pytest.fixture(autouse=True)
def reset_default_company():
    """在每个测试函数运行前，重置 _default_company_data 为初始值"""
    from m06_encapsulate_variable import set_default_company

    initial_data = {"name": "TechCorp", "country": "USA", "founded": 1995}
    set_default_company(initial_data)
    # 测试结束后无需清理，autouse=True 会自动为每个测试重置


def test_create_employee():
    create_employee("Alice", 30)
    assert "Made in USA with pride!" == get_company_slogan()


def test_transfer_company():
    transfer_company("NewWorld Inc", "Canada")
    assert "Global innovation from Canada!" == get_company_slogan()


def test_getter_returns_independent_copy():
    """测试：getter 返回的是副本，外部修改不影响内部"""
    # 获取当前公司信息
    external_ref = default_company()
    assert external_ref["country"] == "USA"

    # 外部修改 getter 返回的对象
    external_ref["country"] = "HackedLand"

    # 再次获取公司信息，应该仍是原始值
    fresh_copy = default_company()
    assert fresh_copy["country"] == "USA"
    assert fresh_copy["country"] != "HackedLand"


def test_setter_isolates_external_mutation():
    """测试：setter 保存的是副本，外部修改不影响内部"""
    # 准备外部数据
    external_data = {"name": "NewWorld", "country": "Canada", "founded": 1995}

    # 设置为默认公司
    set_default_company(external_data)

    # 在 setter 调用后，修改外部数据
    external_data["country"] = "HackedLand"

    # 获取当前公司，应该仍是 "Canada"
    current = default_company()
    assert current["country"] == "Canada"
    assert current["country"] != "HackedLand"


def test_setter_and_getter_are_isolated():
    """测试：多次调用 getter 返回的是不同对象（副本）"""
    set_default_company({"name": "Isolated", "country": "Japan", "founded": 2000})

    obj1 = default_company()
    obj2 = default_company()

    # 两个 getter 返回的对象应该是不同的实例
    assert obj1 is not obj2

    # 修改其中一个，不应影响另一个
    obj1["country"] = "Mutated"
    assert obj2["country"] == "Japan"
