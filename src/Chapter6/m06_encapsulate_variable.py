from types import MappingProxyType

# 全局变量：默认公司信息
_default_company_data = {
    "name": "TechCorp",
    "country": "USA",
    "founded": 1995,
}


def default_company():
    return MappingProxyType(_default_company_data)


def set_default_company(data):
    global _default_company_data
    _default_company_data = data.copy()


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
勘误：之前的提交（23698343, "init the code and tests"）中的测试样例写得不对。
应该像现在这样，测试代码中调用 `create_employee` 和 `transfer_company`，然后通过 `get_company_slogan`
来验证 slogan 是否正确。

原则：对于所有可变的数据，只要它的作用域超出单个函数，就将其封装起来，只允许通过函数访问。数据的作用域越大，封装就越重要。

重构步骤：
1. 为变量的读取和修改编写函数
2. 逐步利用测试将所有的变量引用替换为通过函数访问
3. 修改原始变量的可见性或者改名（例如加前导下划线 `_`，这样可以避免遗漏——如果有遗漏就一定会报错；还可保证之后的代码不会直接访问该变量）

使用副本以提高数据隔离性：
- 当数据来自外部（如用户输入、API 响应、其他模块）时，应在设值函数（setter）中保存其副本（deepcopy 或 copy），防止外部修改影响内部状态。
- 在取值函数（getter）中也应返回副本，防止调用者意外修改内部数据。
- 是否使用副本，取决于是否需要与源数据保持连接：
  - 若需感知源数据变化（如共享配置对象），可保留引用；
  - 若需独立控制生命周期（推荐多数情况），应使用副本。
- 使用 `copy.deepcopy()` 处理嵌套结构，`dict.copy()` 或 `list.copy()` 处理浅层结构。
- 可通过测试验证副本行为：修改 getter 返回值或 setter 输入源后，再次读取应不受影响。
- 对性能敏感的场景，可考虑使用不可变数据结构（如 `types.MappingProxyType`）替代副本，实现零拷贝的安全封装。

✅ 补充说明
为什么“副本”是封装的重要一环？
封装不仅是“用函数包一层”，更是控制数据的所有权和生命周期。
直接传递引用 = 放弃控制权。
使用副本 = 掌握控制权，实现真正的数据隔离。

示例：用 MappingProxyType 实现高效封装（进阶）
```python
from types import MappingProxyType

_default_company_data = {"name": "TechCorp", "country": "USA"}

def default_company():
    return MappingProxyType(_default_company_data)  # 返回只读视图

def set_default_company(data):
    global _default_company_data
    _default_company_data = dict(data)  # 保存副本
```

注：目前的代码还可封装成类来控制 _default_company 的行为，将 `create_employee` 和 `transfer_company` 封装进类中，
但是因为这里主要是在练习“封装变量”的重构手法，所以暂且不深究了。
"""
