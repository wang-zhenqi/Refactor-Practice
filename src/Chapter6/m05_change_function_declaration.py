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


def calculate_user_score(user):
    base_score = user.age * 10
    activity_bonus = user.activity_level * 20
    return base_score + activity_bonus
