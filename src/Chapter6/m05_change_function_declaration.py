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
