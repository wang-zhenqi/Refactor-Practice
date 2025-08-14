def calculate_total_price(items):
    """
    第一阶修改：更改函数名
    """

    total = sum(item["price"] * item["quantity"] for item in items)
    return total


def apply_discount_and_tax(discount_rate, total_price, tax_rate=0.0):
    """
    第二阶修改：增减函数参数
    目标：给函数新增一个 `tax_rate` 参数
    """
    net_rate = 1 - discount_rate
    tax_inclusive_rate = 1 + tax_rate
    return total_price * net_rate * tax_inclusive_rate


def calculate_shipping_cost(weight, distance, rate_per_kg, rate_per_km):
    """
    第二阶修改：增减函数参数
    目标：删除 `abroad` 参数，因为业务方说明不用再区分是否运往海外了，价格统一了
    """
    return round(weight * rate_per_kg + distance * rate_per_km, 2)


class User:
    def __init__(self, name, age, email, activity_level, membership_years):
        self.name = name
        self.age = age
        self.email = email
        self.activity_level = activity_level
        self.membership_years = membership_years


def calculate_user_score(age, activity_level):
    """
    第三阶段修改：把参数改为属性
    这种方法主要适用于原始函数所处理的数据只是参数的某些属性，因此将整个参数都传入就不太合理，
    会让读者误解该函数的用法。通过“把参数改为属性”的方法，只传入实际用到的属性作为参数，
    这样可以降低函数处理的复杂度，提高可读性，同时让函数的使用方式更加具体。
    """
    return age * 10 + activity_level * 20
